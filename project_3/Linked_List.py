class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            """Initialization of the __Node class, setting up the value, previous, and next attributes"""

            # PERFORMANCE:
            # This method is O(1) because regardless of the input to this method only three lines of code will be run.
            # This method just assigns values to constructors.

            # these are public
            self.value = val
            self.previous = None
            self.next = None


    def __init__(self):
        """Initialization of the Linked_List class, setting up the header, trailer, and size attributes"""

        # PERFORMANCE:
        # This method is O(1) because regardless of the input to this method, the method will run these five lines of code.
        # This method just assigns values to constructors.

        # these are private
        self.__header =  Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.previous = self.__header
        self.__size = 0


    def __len__(self):
        """Returns the number of value-containing nodes in the linked list"""

        # PERFORMANCE:
        # This method is O(1) because regardless of the input to this method, the method will only run this one line of code,
        # returning the variable that represents the size of the list.

        return self.__size

    def append_element(self, val):
        """Adds a node at the end of the linked list and increments size by 1"""

        # PERFORMANCE:
        # This method is O(1) because regardless of the value that is input to this method, the performance/runtime
        # of this method is not changed. The method just adds a node in the tail position and corrects the next/previous
        # variables of the nodes that surround it. This is not affected by the size of the linked list.

        # This is the ONLY way to add an item to an empty list or to add an item at the tail of the list

        prior_tail = self.__trailer.previous
        new_node = Linked_List.__Node(val)
        new_node.previous = prior_tail
        prior_tail.next = new_node
        new_node.next = self.__trailer
        self.__trailer.previous = new_node
        self.__size += 1

    def insert_at_head(self, val):
        """Adds a node after the header sentinel node and increments size by 1"""

        # PERFORMANCE:
        # This method is O(1) because regardless of the value that is input into this method, the performance/runtime
        # of this method is not change. This method just adds a node in the head position and corrects the next/previous
        # variable of the nodes that surround it. This is not affected by the size of the linked list.
        
        prior_after_head =  self.__header.next
        new_node = Linked_List.__Node(val)
        new_node.previous = self.__header
        new_node.next = prior_after_head
        self.__header.next = new_node
        prior_after_head.previous = new_node
        self.__size += 1



    def insert_element_at(self, val, index):
        """Inserts a new node with the input value at the input index"""

        # PERFORMANCE:
        # This method is O(n) because as the size of the input list increases, so does the amount of steps this method takes.
        # This linearity is a result of "__position_before_index()" which does a current walk to get to
        # the node before the desired index. Aside from this method call, the rest of the code is constant - a new node is put
        # in place and the next/previous variables of the nodes that surround it are modified and this is not affected by the
        # size of the linked list. Thus the complexity of this method is O(n) as O(n) > O(1).
        # NOTE: the method __position_before_index() has been optimized, see the comments on the method to read more

        # Does a current walk to get to the node before the desired index
        position_before = Linked_List.__position_before_index(self,index)
        position_after = position_before.next
        new_node = Linked_List.__Node(val)

        new_node.next = position_after
        new_node.previous = position_before

        position_before.next = new_node
        position_after.previous = new_node

        self.__size += 1

    def remove_element_at(self, index):
        """Removes the node at the input index"""

        # PERFORMANCE:
        # This method is O(n) because with a larger sized input list, more steps are taken by this method.
        # The linearity of this method is a result of the calling of "__position_before_index()" which
        # does a current walk to get to the node before the desired node. Aside from this method call,
        # the rest of this method is constant - the node at the desired index is removed and the next/previous variables
        # of the nodes surrounding this removed node are altered. This changing of properties is not affected by the size
        # of the linked list, making this part constant. As linear > constant, this method remains O(n).
        # NOTE: the method __position_before_index() has been optimized, see the comments on the method to read more

        # Does a current walk to get to the node before the desired index
        position_before = Linked_List.__position_before_index(self,index)
        ret = position_before.next.value
        hold = position_before.next.next
        position_before.next = hold
        hold.previous = position_before

        self.__size -= 1
        return ret

    def get_element_at(self, index):
        """Returns the value of the node at the input index"""

        # PERFORMANCE:
        # This method is O(n) because with a larger sized input list, this method takes more steps.
        # The linearity of this method is caused by the calling of "__position_before_index()" which
        # does a current walk to get to the node before the desired node. Aside from the method call,
        # the rest of this method is constant - the value of the desired node is returned, and this process
        # is constant. As linear > constant, this method remains O(n).
        # NOTE: the method __position_before_index() has been optimized, see the comments on the method to read more

        # Does a current walk to get to the node before the desired index
        position_before = Linked_List.__position_before_index(self,index)
        return position_before.next.value

    def __position_before_index(self,index):
        """Returns the node at the position before the index that is input"""

        # PERFORMANCE:
        # This method is O(n) because as the input list gets larger, the amount of steps this
        # method takes increases. This method does a current walk to get to the node before the
        # desired index, and this walk increases in the worst case as the amount of nodes increases.
        # This method was split in two parts to increase efficiency. In the worst case scenario it
        # now takes half as long as it would have if it had started from the header node. 

        # Catches and raises an error if the desired index is outide the bounds of the list
        if index < 0 or index >= self.__size:
            raise IndexError
        
        # Since I'm returning the position BEFORE the desired index, I used <= self.__size / 2 rather than
        #  < self.__size / 2, to include the following kind of scenario: there are 8 elements in the 
        # list, 8/2=4, to get the position before index 4, there are only 4 steps to get there from 
        # the header, while it would take 5 to get there from the trailer.

        if(index <= self.__size / 2):
            current = self.__header
            for i in range(index):
                current = current.next
        else:
            current = self.__trailer
            for i in range(self.__size - index + 1):
                current = current.previous
        return current

    def rotate_left(self):
        """Rotates each node in the linked list left one position"""

        # PERFORMANCE:
        # This method is O(1). Regardless of how large the input list is, this method just
        # moves the node after the header to be in the position before the trailer, modifying
        # the next/previous attributes of the affected nodes and this remains a constant runtime
        # no matter how long the linked list becomes.


        if self.__size > 1:
            moving_node = self.__header.next
            new_first = moving_node.next
            self.__header.next = new_first
            new_first.previous = self.__header

            moving_node.next = self.__trailer
            second_to_last = self.__trailer.previous
            second_to_last.next = moving_node
            moving_node.previous = second_to_last
            self.__trailer.previous = moving_node
        
    def __str__(self):
        """Returns the string representation of the list's contents"""

        # PERFORMANCE:
        # This method is O(n). In the worst case scenario, the method has to use
        # a for loop to iterate through all of the nodes in the list, and as the
        # size of the list increases, so does the amount of steps taken by this
        # method.

        # returns [ ] when the list is empty
        if self.__size == 0:
            return "[ ]"
        
        # returns [ 5 ] when 5 is the only element, or [ 5, 7 ] when 5 and 7
        # are elements. This format continues for larger list sizes.
        ret = "[ "
        ret += ", ".join(str(value) for value in self)
        ret += " ]"
        #for i in range(self.__size):
        #    added = ", ".join(cur.value)
        #    ret = added.join(ret)
        #    cur = cur.next
        #ret = ret[:-2]
        #ret += " ]"
        return ret
        # USE JOIN METHOD TO MAKE THIS LINEAR !!!!!!

    def __iter__(self):
        """Initializes a new attribute allowing iteration through the linked list"""

        # PERFORMANCE:
        # This method is O(1). Regardless of the size of the linked list, this method
        # remains constant. The method just sets up an iter node and returns the linked
        # list.

        self.__iter_node = self.__header.next
        return self

    def __next__(self):
        """Fetches the next value in the linked list and returns it. If there are no more values StopIteration is raised"""

        # PERFORMANCE:
        # This method is O(1). Regardless of the size of the linked list, this method
        # remains constant. The method just checks to see if the current node is the trailer,
        # and if it isn't then the iter node is changed to be the next node in the sequence.

        if self.__iter_node is self.__trailer:
            raise StopIteration
        to_return = self.__iter_node.value
        self.__iter_node = self.__iter_node.next
        return to_return

    def __reversed__(self):
        """Constructs and returns a new Linked_List object whose nodes are the reverse order of the linked list passed through"""

        # PERFORMANCE:
        # This method is O(n). This method uses a for loop to iterate through all
        # of the nodes in the list, so with more elements in the list, more steps are
        # taken/executed. This method also calls append_element(), and because
        # append_element() is constant, it doesn't make the performance of this method
        # worse than O(n).

        reversed_ll =  Linked_List()
        current = self.__trailer.previous

        for i in range(self.__size):
            reversed_ll.append_element(current.value)
            current = current.previous

        return reversed_ll
    
    def __check_structure(self):
        """Checks if the structure of the linked list is correct"""

        # PERFORMANCE:
        # This method is O(n) because as the input linked list increases in size, more steps are taken
        # to check the list in the while loops. There are two while loops that are each linear, and a final
        # for loop that is also linear. None are nested, so the performance remains O(n).

        # I created this method so that I could check that the structure of the linked list is not altered
        # after modifications. This method uses two while loops, one to loop from header to trailer, and
        # the other to loop from trailer to header. If any of the nodes between the header or trailer point
        # to None, this indicates there is an error, and a ValueError is raised. A RuntimeError is also raised
        # in the event that the linked list is circular. After both while loops I also check that the values 
        # from the two while loops match, meaning that the order of the linked list flows as it's expected.
        # NOTE: There weren't enough unique exceptions for me to raise, and I'm not sure if you're able to
        # slap random exceptions for various things, so if there is an exception raised it can be hard to pinpoint
        # the problem - though I added a simple print statement to expedite this.

        forwards = []
        backwards = []
        current_node = self.__header.next
        count = 0
        while current_node is not self.__trailer:
            count += 1
            forwards.append(current_node.value)
            # this if statement checks to make sure that only the header and trailer point to None
            if current_node.next == None:
                print("node points to None")
                raise ValueError
            
            # This if statement checks if the linked list is circular in any way. If it is, that means that nodes
            # reference previous nodes that they shouldn't, and if that is the case, this while loop will run infinitely.
            # This statement ensures that the while loop doesn't loop forever in the event the linked list is circular.
            elif count > self.__size:
                print("circular linked list")
                raise RuntimeError
            
            current_node = current_node.next
        
        current_node = self.__trailer.previous
        count = 0
        while current_node is not self.__header:
            count += 1
            backwards.append(current_node.value)
            # this if statement checks to make sure that only the header and trailer point to None
            if current_node.previous == None:
                print("node points to None")
                raise ValueError
            
            # This if statement checks if the linked list is circular in any way. If it is, that means that nodes
            # reference previous nodes that they shouldn't, and if that is the case, this while loop will run infinitely.
            # This statement ensures that the while loop doesn't loop forever in the event the linked list is circular.
            elif count > self.__size:
                print("circular linked list")
                raise RuntimeError
            
            current_node = current_node.previous
        
        # Checking that the order going forwards and backwards remains consistent
        if(forwards == list(reversed(backwards))):
            printed = ""
            for val in forwards:
                printed += str(val) + " | "

            if(len(printed) > 0):
                print("This linked list has the correct structure, and has values:")
                printed = printed[:-3]
                print(printed)
            else:
                print("This linked list has the correct structure and is empty.")
        
        else:
            print("forwards and backwards don't match")
            print(forwards)
            print(backwards)
            raise ValueError

    def try_check_structure(self):
        """Uses check_structure to check for any errors"""

        # PERFORMANCE:
        # This method is O(n) - the same as check_structure() because all it does is call
        # check_structure() inside of a try - except block

        # I put this into its own method because I would've been copying and
        # pasting the same code repeatedly otherwise.

        try:
            self.__check_structure()
        except ValueError:
            print("Error: unexpected point to None or forwards/backwards don't match up")
        except RuntimeError:
            print("Error: unexpected circular array.")
        

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests


    # *---* Begin test 1 *---*

    # Showing that appending adds to the end of the list, as well as showing the functionality of __str__ by printing the list
    # I didn't use try except here because append_element doesn't raise any exceptions - should I do a try except here?
    print("*---* Begin test 1 *---*\n")
    ll = Linked_List()
    # Showing __str__ works correctly for a blank list
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Appending 1:")
    ll.append_element(1)
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Appending 2:")
    ll.append_element(2)
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Appending 3:")
    ll.append_element(3)
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Appending 4:")
    ll.append_element(4)
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Appending 5:")
    ll.append_element(5)
    print(ll)
    print("List size: " + str(len(ll)) + "\n")

    print("Checking that append correctly modified the list's structure:")
    ll.try_check_structure()

    print("\n*---* End test 1 *---*")

    # *---* End test 1 *---*
    
    print("\n\n")

    # *---* Begin test 2 *---*

    # To show that both __iter__ and __next__ work:
    print("*---* Begin test 2 *---*\n")

    ll2 = Linked_List()
    ll2.append_element(11)
    ll2.append_element(22)
    ll2.append_element(33)
    ll2.append_element(44)
    ll2.append_element(55)
    
    print("Showing that the for loop works correctly:")
    for val in ll2:
        print(str(val))

    print("\n*---* End test 2 *---*")

    # *---* End test 2 *---*
    
    print("\n\n")

    # *---* Begin test 3 *---*

    # Showing that inserting an item at a valid index increases the size by one and correctly modifies the list's structure by using a for loop:
    print("*---* Begin test 3 *---*\n")

    ll3 = Linked_List()
    ll3.append_element(111)
    ll3.append_element(222)
    ll3.append_element(333)
    ll3.append_element(444)
    ll3.append_element(555)

    print("Unmodified list:")
    print(ll3)
    print("Length of the list: " + str(len(ll3)) + "\n")

    # Testing inserting
    print("Testing insertion at valid indexes:")
    try:
        # These should all work without any errors
        ll3.insert_element_at("x",0)
        ll3.insert_element_at("y",3)
        ll3.insert_element_at("z",6)
    except IndexError:
        print("Error: Unexpected index out of bounds error")
    print(ll3)
    print("Length of the list: " + str(len(ll3)) + "\n")

    print("Checking that the structure of the linked list was correctly modified after valid insertion:")
    ll3.try_check_structure()
    print()

    print("Testing insertion at an invalid index:")
    try:
        # This should fail as 8 is out of bounds
        ll3.insert_element_at("f", 8)
    except IndexError:
        print("Correctly caught out of bounds error. No crash")
    print(ll3)
    print("Length of the list: " + str(len(ll3)) + "\n")

    print("Checking that the structure of the linked list wasn't modified after invalid insertion:")
    ll3.try_check_structure()
    print()

    print("Testing removal at valid indexes (I'm removing the previously inserted 'x', 'y', 'z')")
    # Testing removing
    try:
        # These should all work without any errors
        ll3.remove_element_at(6)
        ll3.remove_element_at(3)
        ll3.remove_element_at(0)
    except IndexError:
        print("Error: Unexpected out of bounds error")
    print(ll3)
    print("Length of the list: " + str(len(ll3)) + "\n")

    print("Checking that the structure of the linked list was correctly modified after valid removal:")
    ll3.try_check_structure()
    print()

    print("Testing removal at an invalid index:")
    try:
        # This should fail as 5 is out of bounds
        ll3.remove_element_at(5)
    except IndexError:
        print("Correctly caught out of bounds error. No crash")
    print(ll3)
    print("Length of the list: " + str(len(ll3)) + "\n")

    print("Checking that the structure of the linked list wasn't modified after invalid removal:")
    ll3.try_check_structure()
    print()
    
    print("*---* End test 3 *---*")
    
    # *---* End test 3 *---*

    print("\n\n")

    # *---* Begin test 4 *---*

    print("*---* Begin test 4 *---*\n")

    ll4 = Linked_List()
    print("Attempting to insert an element into an empty list:")
    try:
        # Inserting an element into an empty linked list - this is not allowed
        ll4.insert_element_at(0,0)
    except IndexError:
        print("Correctly caught out of bounds error. No crash")
    
    print("Checking that the structure isn't affected after an invalid insertion:")
    ll4.try_check_structure()

    print()

    print("Attempting to remove an element from an empty list:")
    try:
        ll4.remove_element_at(0)
    except IndexError:
        print("Correctly caught out of bounds error. No crash")

    print("Checking that the structure isn't affected after an invalid removal:")
    ll4.try_check_structure()

    # Testing insertion and removal on an empty list, both should be errors. Check structure after each test to ensure structure remains correct.

    print("\n*---* End test 4 *---*")

    # *---* End test 4 *---*

    print("\n\n")


    # *---* Begin test 5 *---*

    # Showing that reversed works as expected
    print("*---* Begin test 5 *---*\n")

    ll5 = Linked_List()
    ll5.append_element("A")
    ll5.append_element("B")
    ll5.append_element("C")
    ll5.append_element("D")
    ll5.append_element("E")

    # Showing the for loop works for the regular linked list
    print("Regular:")
    for val in ll5:
        print(val)

    # Showing the for loop works for the reversed linked list
    print("\nReversed:")
    for val in reversed(ll5):
        print(val)

    print()
    ll5 = reversed(ll5)
    print(ll5)
    print("Checking that reversing a linked list doesn't mess up its structure:")
    ll5.try_check_structure()
    

    print("\n*---* End test 5 *---*")

    # *---* End test 5 *---*

    print("\n\n")

    # *---* Begin test 6 *---*

    print("*---* Begin test 6 *---*\n")

    ll6 = Linked_List()
    ll6.append_element(0)
    ll6.append_element(1)
    ll6.append_element(2)
    ll6.append_element(3)
    ll6.append_element(4)

    print(ll6)
    print("Testing get element at valid indexes:")
    try:
        print("Element at index 1: " + str(ll6.get_element_at(1)))
        print("Element at index 3: " + str(ll6.get_element_at(3)))
    except IndexError:
        print("Unexpected index error")

    print()
    print(ll6)
    print("Checking that the structure wasn't altered after doing a valid get element:")
    ll6.try_check_structure()

    print("\nAttempting to get element at an invalid index:")
    try:
        print("Element at index 5:" + str(ll6.get_element_at(5)))
    except IndexError:
        print("Correctly caught index out of bounds error.")

    print()
    print(ll6)
    print("Checking that the structure wasn't altered after doing an invalid get element:")
    ll6.try_check_structure()

    print("\n*---* End test 6 *---*")

    # *---* End test 6 *---*