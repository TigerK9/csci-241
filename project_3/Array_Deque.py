from Deque import Deque

class Array_Deque(Deque):

    def __init__(self):
        """Initialization of an array based deque"""

        # PERFORMANCE:
        # This method is constant O(1), as it executes the same amount of code every time
        # it's called and is not affected by the amount of data in the deque

        # capacity starts at 1; this is grown on demand using __grow
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        self.__front_index = 0
        self.__back_index = 0
        self.__size = 0
        
    def __str__(self):
        """Returns the string representation of the array based deque"""

        # PERFORMANCE:
        # This method is linear O(n), as with a larger amount of data in the 
        # deque, this method executes more lines of code. This linearity is caused
        # by the for loop that iterates through the array to put it into a string that 
        # can be returned.

        # This method returns a string representation of the deque from its front (left)
        # to its back (right). An empty deque looks like this: [ ]
        # A deque with one item looks like: [ item ]
        # A deque with two items looks like: [ item, item ]
        # This pattern continues for all amounts of items in the deque.
        if self.__size == 0:
            return "[ ]"
        
        ret = "[ "
        ret += ", ".join(str(self.__contents[(i+self.__front_index) % self.__capacity]) for i in range(self.__size))
        ret += " ]"
        return ret
        
    def __len__(self):
        """Returns an integer representing the amount of items in the array based deque"""
        
        # PERFORMANCE:
        # This method is constant O(1), as regardless of the size of the deque, only one line of code
        # is executed. By keeping track of the size of the deque in a size variable as different methods
        # are called, this allows the len method to be constant.

        return self.__size

    def __grow(self):
        """Doubles the capacity of the array used by the deque and reformats it to start with the front at cell 0"""
        
        # PERFORMANCE:
        # This method is linear O(n), as with a larger amount of items in the array (represented by the size variable)
        # before the array is unwrapped and reformatted, more lines of code are executed. This is due to the for loop
        # that iterates from front to back of the original array, reformatting it.

        self.__capacity = self.__capacity * 2
        # A copy of the original array is made so that the actual array can be modified, though its information is still
        # able to be accessed in its original order.
        temporary_contents = self.__contents[:]
        self.__contents = [None] * self.__capacity
        for i in range(self.__size):
            self.__contents[i] = temporary_contents[self.__front_index]
            self.__front_index = (self.__front_index + 1) % self.__size
        # The front and back index variables must be changed after the unraveling of the original deque.
        self.__front_index = 0
        self.__back_index = self.__size - 1

        
    def push_front(self, val):
        """Adds a new item at the front of the deque"""

        # PERFORMANCE:
        # This method is linear O(n), as it calls the grow method which is linear, causing this method to also be
        # linear. The rest of this method is constant, and as constant < linear, the method is linear.


        # If the size is the same as the capacity, this means that there won't be enough cells to push more data into
        # the array, and thus it must be grown.
        if self.__size == self.__capacity:
            self.__grow()

        # The front index is decremented by 1 to move the front index back 1, then the capacity is added to this number to
        # avoid negative indexes. Then this is modulused by the capacity to create a circular property in the array, allowing the
        # array to loop from front to back.
        self.__contents[(self.__front_index - 1 + self.__capacity) % self.__capacity] = val
        self.__front_index = (self.__front_index - 1 + self.__capacity) % self.__capacity
        self.__size += 1
        
    def pop_front(self):
        """Removes the item at the front of the deque"""

        # PERFORMANCE:
        # This method is constant O(1), because regardless of how large or small the deque grows to, the amount of executions by this
        # method is not effected.

        if self.__size == 0:
            return
        else:
            returned = self.__contents[self.__front_index]
            # The front index is incremented by 1, then this is modulused by the capacity to allow for the circular property
            # of the array used for the deque.
            self.__front_index = (self.__front_index + 1) % self.__capacity
            self.__size -= 1
            return returned
        
    def peek_front(self):
        """Returns the item at the front of the deque"""

        # PERFORMANCE:
        # This method is constant O(1), because regardless of how large or small the deque grows to, the amount of executions by
        # this method is not effected.

        if self.__size == 0:
            return
        else:
            return self.__contents[self.__front_index]
        
    def push_back(self, val):
        """Adds a new item at the back of the deque"""

        # PERFORMANCE:
        # This function is linear O(n), as it calls the grow function which is linear, causing this function to be linear.
        # The rest of this method is constant, so as linear > constant, this method is linear.

        # If the size is the same as the capacity, this means that there won't be enough cells to push more data into
        # the array, and thus it must be grown.
        if self.__size == self.__capacity:
            self.__grow()
  
        # The back index is incremented by 1 to move the back index forward 1, then this number is modulused by the
        # capacity allowing for the circular property of the array. The array is able to loop from back to front this way. 
        self.__contents[(self.__back_index + 1) % self.__capacity] = val
        self.__back_index = (self.__back_index + 1) % self.__capacity
        self.__size += 1
    
    def pop_back(self):
        """Removes the item at the back of the deque"""

        # PERFORMANCE:
        # This function is constant O(1), as the amount of executions by this method remain the same regardless of how large
        # or small the deque is.

        # The back index is decremented by 1, then the capacity is added to this number to prevent negative indexes from
        # occuring, then this number is modulused by the capacity to allow for the circular property of the array.
        if self.__size == 0:
            return
        else:
            returned = self.__contents[self.__back_index]
            self.__back_index = (self.__back_index - 1 + self.__capacity) % self.__capacity
            self.__size -= 1
            return returned

    def peek_back(self):
        """Returns the item at the back of the deque"""

        # PERFORMANCE:
        # This function is constant O(1), as the amount of executions by this method remain the same regardless of how
        # large or small the deque is. The cell in the array at __back_index is found, and this value is returned, which
        # occurs in constant run time.

        if self.__size == 0:
            return
        else:
            return self.__contents[self.__back_index]

# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
    pass