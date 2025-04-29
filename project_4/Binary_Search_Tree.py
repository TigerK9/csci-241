class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            """Initialization of a new node"""
            
            # PERFORMANCE:
            # This method is constant O(1), because only these four lines of code run every time this method is
            # called, not ever doing any more or less. This method just assigns values to the constructors.

            self.value = value
            self.height = 1
            self.right = None
            self.left = None

    def __init__(self):
        """Initialization of a new binary search tree"""

        # PERFORMANCE:
        # This method is constant O(1), because it only executes this one line of code. The root (a constructor)
        # is set to None, and nothing else happens in this method.

        self.__root = None

    def insert_element(self, value):
        """A new node a created and inserted into the tree containing the value passed into this method"""
        # This method inserts new values based on the BST ordering of less is left, greater is right. If the value
        # is already in the tree, a ValueError is raised. 

        # PERFORMANCE:
        # This method is logarithmic O(log(n)), as it just calls the recursive insert method, which is
        # O(log(n)) - see __recursive_insert() for further explanation.

        self.__root = self.__recursive_insert(value, self.__root)

    def __recursive_insert(self, value, t):
        """Private method that facilitates insertion recursively"""

        # PERFORMANCE:
        # This method is logarithmic, O(log(n)). Since the tree is balanced, the deepest a node will be inserted is
        # at log(n) steps from the root

        # If there is None where a node would go next, then this is the base case and a new node needs to be
        # created here.
        if t == None:
            t = self.__BST_Node(value)

        # If the value is less than t's value, it should be inserted at the left of t, so the recursive
        # insert function is called using the same value though now with t.left as the node t.
        elif value < t.value:
            t.left = self.__recursive_insert(value, t.left)

        # If the value is greater than t's value, it should be inserted at the right of t, and the recursive
        # insert function is called using the same value but now with t.right as the node t.
        elif value > t.value:
            t.right = self.__recursive_insert(value, t.right)

        # If the node is not None, and is not greater or less than t, that means the value is at node t, and is
        # a duplicate, where a ValueError will be raised.
        else:
            raise ValueError
        
        return self.__balance(t)
    
    def __update_height(self, t):
        """Updates the height of a node using its two children as references to do so"""

        # PERFORMANCE:
        # This function by itself is constant O(1). All that's done is the height values of the node t's two children
        # are checked, and the value of t is updated accordingly. There are no recursive calls within this function, and each
        # call of t.right or t.left is constant. The function max() is inherently O(n), though since only two items are put into the
        # function, this method remains O(1), because max() would always be O(2) here (where n = 2 and never more).

        if t == None:
            return
        
        elif t.left == None and t.right == None:
            return 1
        elif t.left == None:
            return t.right.height + 1
        elif t.right == None:
            return t.left.height + 1
        else:
            return max(t.left.height, t.right.height) + 1

    def remove_element(self, value):
        """Removes the node containing the value passed into this method"""
        
        #PERFORMANCE:
        # This method is logarithmic O(log(n)), as it simply calls the __recursive_remove() method to remove a node, which is O(log(n)).
        # See the __recursive_remove() method for further analysis.
        
        self.__root = self.__recursive_remove(value, self.__root)

    def __recursive_remove(self, value, t):
        """Private method that facilitates recursive node removal"""

        # PERFORMANCE:
        # This method is logarithmic O(log(n)). The deepest this method will go is to a leaf to remove said leaf. The deepest this leaf can
        # possibly be is log(n) steps from the root, because this tree is balanced. Thus in the worst case, this method will take log(n) steps.

        if t == None:
            raise ValueError
        
        elif value == t.value:
            if t.left != None and t.right != None:

                # find smallest on right of tree
                smallest = t.right
                while smallest.left != None:
                    smallest = smallest.left

                # smallest is the smallest value of the right subtree
                t.value = smallest.value
                t.right = self.__recursive_remove(smallest.value, t.right)

            elif t.left == None:
                t = t.right
            else:
                t = t.left

        elif value < t.value:
            t.left = self.__recursive_remove(value, t.left)
        elif value > t.value:
            t.right = self.__recursive_remove(value, t.right)

        return self.__balance(t)
    
    def __balance(self, t):
        """Balances the subtree rooted at the node passed into this method"""

        # PERFORMANCE:
        # This method is constant O(1). This method calls the __get_balance_factor() method which runs in constant time,
        # and in the worst case scenario, calls two rotate's, and all of the rotates run in constant time as well. Finally this
        # method calls __update_height() which also runs in constant time. This means that overall, in the worst case, this method is constant.

        if t == None:
            return t

        balance_factor = self.__get_balance_factor(t)

        # right heavy by 2
        if balance_factor == 2:
            right_child_balance = self.__get_balance_factor(t.right)

            # rotate left about t and return the new root.
            if right_child_balance == 1 or right_child_balance == 0:
                t = self.__rotate_left_about_node(t)

            # rotate right about t’s right child, then rotate left about t and return the new root.
            else:
                t.right = self.__rotate_right_about_node(t.right)
                t = self.__rotate_left_about_node(t)

        # left heavy by 2
        elif balance_factor == -2:
            left_child_balance = self.__get_balance_factor(t.left)

            # rotate right about t and return the new root.
            if left_child_balance == -1 or left_child_balance == 0:
                t = self.__rotate_right_about_node(t)

            # rotate left about t's left child, then rotate right about t and return the new root.
            else:
                t.left = self.__rotate_left_about_node(t.left)
                t = self.__rotate_right_about_node(t)

        t.height = self.__update_height(t)
        return t
    
    def __rotate_left_about_node(self, t):
        """Left rotation of the subtree rooted at the node passed into this method allowing for the implementation of a balanced BST"""

        # PERFORMANCE:
        # This method is constant O(1). This method simply rearranges the values within the subtree rooted at t
        # rotating them left. There are multiple aliases and new variables created, and this all occurs in constant
        # time. There is also a call of __update_height(t), though as this method is also constant, this doesn't affect
        # the overall performance of this method.

        new_root = t.right
        floater = new_root.left
        t.right = floater
        new_root.left = t
        t.height = self.__update_height(t)

        return new_root

    def __rotate_right_about_node(self, t):
        """Right rotation of the subtree rooted at the node passed into this method allowing for the implementation of a balanced BST"""

        # PERFORMANCE:
        # This method is constant O(1). This method simply rearranged the values within the subtree rooted at t,
        # rotating them right. Within this method there are muletiple aliases and new variables created, and this all occurs
        # in constant time. There's also a coll of __update_height(t), and this method is also constant, meaning the overall
        # performance ins't affected, and the runtime of this method remains constant O(1).

        new_root = t.left
        floater = new_root.right
        t.left = floater
        new_root.right = t
        t.height = self.__update_height(t)

        return new_root


    def __get_balance_factor(self, t):
        """Returns the balance factor of the node that is passed into this method"""

        # PERFORMANCE:
        # This method is constant O(1). Within this method there are multiple calls of t.left, t.right, and the 
        # heights of these two as well. All of these calls are constant, and the rest of this method is also constant,
        # so overall this method runs in constant time.

        if t.left == None and t.right == None:
            return 0
        elif t.left == None:
            return t.right.height
        elif t.right == None:
            return (0 - t.left.height)
        else:
            return (t.right.height - t.left.height)

    def in_order(self):
        """Returns the string representation of the in-order traversal of the BST"""
        # The returned string is in the format of
        # - Empty tree: [ ]
        # - Tree with one node: [ 1 ]
        # - Tree with two nodes: [ 1, 2 ]
        # and so on.
        
        # PERFORMANCE
        # This method is quadratic O(n^2). The call of __recursive_in_order() makes this method O(n^2), as O(n^2) > O(n).
        # The return of concatenating "[ " and " ]" to the ends of returned would be O(n), but since __recursive_in_order() is
        # O(n^2), this method is O(n^2).

        returned = self.__recursive_in_order(self.__root)
        if len(returned) == 0:
            return "[ ]"
        return "[ " + returned + " ]"

    def __recursive_in_order(self,t):
        """Private method that facilitates the recursive returning of a string representing the in-order traversal of the BST"""

        # PERFORMANCE:
        # This method is quadratic O(n^2). This is because of the constant string concatenation that's returned. Each string concatenation
        # take n steps, and if there are n nodes to be returned in an in-order traversal, this would take n*n steps = n^2.

        # Base case, returns an empty string
        if t == None:
            return ""
        
        # Putting the left and right subtrees into a string variable so they can be checked, allowing
        # for correct formatting
        left = self.__recursive_in_order(t.left)
        right = self.__recursive_in_order(t.right)
        node = str(t.value)
        # If both the left and right subtrees are empty, there only needs to be the node itself returned
        if len(left) == 0 and len(right) == 0:
            return node
        elif len(left) == 0:
            return node + ", " + right
        elif len(right) == 0:
            return left + ", " + node
        else:
            return left + ", " + node + ", " + right

    def pre_order(self):
        """Returns the string representation of the pre-order traversal of the BST"""

        # PERFORMANCE:
        # This method is quadratic O(n^2) due to its calling of __recursive_pre_order() which is O(n^2). The rest of this function
        # due to the concatenation of brackets to returned takes n steps, though since n^2 > n, this method overall is O(n^2).

        returned = self.__recursive_pre_order(self.__root)
        if len(returned) == 0:
            return "[ ]"
        return "[ " + returned + " ]"

    def __recursive_pre_order(self, t):
        """Private method that facilitates the recursive returning of a string representing the pre-order traversal of the BST"""

        # PERFORMANCE:
        # This method is quadratic O(n^2). Each concatenation here takes n steps, and as this method is called recursively, if there are
        # n nodes to be traversed, this method would take n*n steps, or n^2 steps.
 
        if t == None:
            return ""
        
        left = self.__recursive_pre_order(t.left)
        right = self.__recursive_pre_order(t.right)
        node = str(t.value)

        if len(left) == 0 and len(right) == 0:
            return node
        elif len(left) == 0:
            return node + ", " + right
        elif len(right) == 0:
            return node + ", " + left
        else:
            return node + ", " + left + ", " + right

    def post_order(self):
        """Returns the string representation of the post-order traversal of the BST"""
       
       # PERFORMANCE:
       # This method is quadratic O(n^2) because it calls the __recursive_post_order() method which is O(n^2). The rest of this method,
       # particularly the concatenation of brackets, would take at most n steps. Since n^2 > n, this method overall is O(n^2).

        returned = self.__recursive_post_order(self.__root)
        if len(returned) == 0:
            return "[ ]"
        return "[ " + returned + " ]"

    def __recursive_post_order(self, t):
        """Private method that facilitates the recursive returning a string representing the post-order traversal of the BST"""

        # PERFORMANCE:
        # This method is quadratic O(n^2). This is because each call of this method would take n steps because of the concatenation that
        # occurs here. If there were n nodes, this would occur n times. So this would be n*n, and overall this method would be O(n^2).

        if t == None:
            return ""
        
        left = self.__recursive_post_order(t.left)
        right = self.__recursive_post_order(t.right)
        node = str(t.value)

        if len(left) == 0 and len(right) == 0:
            return node
        elif len(left) == 0:
            return right + ", " + node
        elif len(right) == 0:
            return left + ", " + node
        else:
            return left + ", " + right + ", " + node
        
    def to_list(self):
        """Returns a python list/array containing the in-order traversal of the BST"""
        
        # PERFORMANCE:
        # This method is linear O(n) as it simply calls and returns the __recursive_in_order_list() method, which is linear, making
        # this method also linear.

        returned = self.__recursive_in_order_list(self.__root)
        return returned
    
    def __recursive_in_order_list(self, t):
        """Private method that facilitates the recursive returning of a python list representing the in-order traversal of the BST"""

        # PERFORMANCE:
        # This method is linear O(n). Each append in this is O(1), and each extend is O(k), where k is the number of elements being extended
        # by. This method doesn't append/extend more than what's in the BST, so overall this method would take at most n steps. Since each run of this
        # method is constant, and since this would only run enough time to cover each node, say n nodes, n * 1 = n. This method is O(n)

        returned = []

        if t == None:
            return "end"
        
        left = self.__recursive_in_order_list(t.left)
        right = self.__recursive_in_order_list(t.right)
        node = t.value

        if left == "end" and right == "end":
            returned.append(node)
            return returned
        elif left == "end":
            returned.append(node)
            returned.extend(right)
            return returned
        elif right == "end":
            returned.extend(left)
            returned.append(node)
            return returned
        else:
            returned.extend(left)
            returned.append(node)
            returned.extend(right)
            return returned

    def get_height(self):
        """Returns an integer representing the height of the BST"""

        # PERFORMANCE:
        # This method is constant O(1). If there is no root, then the height of 0 is returned. Otherwise, the height
        # of the root node is returned. Since the height of each node is updated after every insertion/removal, this method
        # simply has to call the value of self.__root.height and return this value, which takes constant time.

        if self.__root == None:
            return 0
        else:
            return self.__root.height

    def __str__(self):
        """Returns the string representing the in-order traversal of the BST"""

        # PERFORMANCE:
        # This method is quadratic O(n^2), as it simply calls the in_order() function, which functions at O(n^2), making this
        # method have the same performance.

        return self.in_order()

if __name__ == '__main__':
    pass
    #unit tests make the main section unnecessary.



