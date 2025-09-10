class Binary_Search_Tree:
    # TODO.I have provided the public method skeletons. You will need
    # to add private methods to support the recursive algorithms
    # discussed in class

    class __BST_Node:
        # TODO The Node class is private. You may add any attributes and
        # methods you need. Recall that attributes in an inner class 
        # must be public to be reachable from the the methods.

        def __init__(self, value):
            # TODO complete Node initialization
            self.value = value
            self.height = 1
            self.right = None
            self.left = None

    def __init__(self):
        self.__root = None
        # TODO complete initialization

    def insert_element(self, value):
        # Insert the value specified into the tree at the correct
        # location based on "less is left; greater is right" binary
        # search tree ordering. If the value is already contained in
        # the tree, raise a ValueError. Your solution must be recursive.
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        # TODO replace pass with your implementation
        self.__recursive_insert(value, self.__root)

    def __recursive_insert(self, value, t):
        # If there is None where a node would go next, then this is the base case and a new node needs to be
        # created here.
        if t == None:
            t = self.__BST_Node(value)

        # If the value is less than t's value, it should be inserted at the left of t, so the recursive
        # insert function is called using the same value though now with t.left as the node t.
        elif value < t.value:
            t.left = self.__recursive_insert(self, value, t.left)

        # If the value is greater than t's value, it should be inserted at the right of t, and the recursive
        # insert function is called using the same value but now with t.right as the node t.
        elif value > t.value:
            t.right = self.__recursive_insert(self, value, t.right)

        # If the node is not None, and is not greater or less than t, that means the value is at node t, and is
        # a duplicate, where a ValueError will be raised.
        else:
            raise ValueError
        return t

    def remove_element(self, value):
        # Remove the value specified from the tree, raising a ValueError
        # if the value isn't found. When a replacement value is necessary,
        # select the minimum value to the from the right as this element's
        # replacement. Take note of when to move a node reference and when
        # to replace the value in a node instead. It is not necessary to
        # return the value (though it would reasonable to do so in some 
        # implementations). Your solution must be recursive. 
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        pass # TODO replace pass with your implementation

    def in_order(self):
        # Construct and return a string representing the in-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed as [ 4 ]. Trees with more
        # than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        pass # TODO replace pass with your implementation

    def pre_order(self):
        # Construct and return a string representing the pre-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        pass # TODO replace pass with your implementation

    def post_order(self):
        # Construct an return a string representing the post-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        pass # TODO replace pass with your implementation

    def to_list(self):
        # Construct and return a Python list/array containing the in-order
        # traversal of the tree. Your solution must be recursive. This will
        # involve the introduction of additional private methods to support
        # the recursion control variable.
        pass # TODO replace pass with your implementation

    def get_height(self):
        # return an integer that represents the height of the tree.
        # assume that an empty tree has height 0 and a tree with one
        # node has height 1. This method must operate in constant time.
        pass # TODO replace pass with your implementation

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
    pass #unit tests make the main section unnecessary.

