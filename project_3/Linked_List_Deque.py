from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    """Initialization of a linked list based deque"""

    # PERFORMANCE:
    # This method is constant O(1), as it only calls the initialization of a linked list, which is also
    # constant, meaning that this method runs in constant time.

    self.__list = Linked_List()

  def __str__(self):
    """Returns the string representation of the linked list based deque"""

    # PERFORMANCE:
    # This method is linear O(n), as it calls the __str__ method from the Linked_List file, which runs in linear
    # time, meaning that this method also runs in linear time.

    return str(self.__list)

  def __len__(self):
    """Returns an integer representing the amount of items in the linked list based deque"""

    # PERFORMANCE:
    # This method is constant O(1), as it calls the __len__ method from the Linked_List file, which runs in
    # constant time, meaning that this method also runs in constant time.

    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    """Adds a new item at the front of the deque"""

    # PERFORMANCE:
    # This method is constant O(1), as this method calls the insert_at_head method from the Linked_List file,
    # which runs at constant time, making this method also run in constant time.

    self.__list.insert_at_head(val)
  
  def pop_front(self):
    """Removes the item at the front of the deque"""

    # PERFORMANCE:
    # This method is constant O(1). This method calls the remove_element_at method from the Linked_List
    # file which runs in linear time, though because the index input into the method is 0, this means that the
    # for loop within the remove_element_at (further the __position_before_index) method is not affected by the
    # amount of items in the linked list, and this method runs the same amount of time regardless of how many or
    # how few items there are in the linked list.

    if len(self.__list) == 0:
      return None

    returned = self.__list.remove_element_at(0)
    return returned

  def peek_front(self):
    """Returns the item at the front of the deque"""

    # PERFORMANCE:
    # This method is constant O(1). This method calls the get_element_at method from the Linked_List
    # file which runs in linear time, though because the index input into the method is 0, this means that the
    # for loop within the get_element_at (further the __position_before_index) method is not affected by 
    # the amount of items in the linked list, and this method runs the same amount of time regardless of how many
    # or how few items there are in the linked list.

    if len(self.__list) == 0:
      return None

    return self.__list.get_element_at(0)

  def push_back(self, val):
    """Adds a new item at the back of the deque"""

    # PERFORMANCE:
    # This method is constant O(1), as it calls the append_element method from the Linked_List file
    # which runs in constant time, meaning that this method also runs in constant time.

    self.__list.append_element(val)
  
  def pop_back(self):
    """Removes the element at the back of the deque"""

    # PERFORMANCE:
    # This method is constant O(1). This method calls the remove_element_at method from the Linked_List
    # file, which runs in linear time, though because the index that's being removed is the last index,
    # and because the __position_before_index method has been optimized (making it start iterating from 
    # the front or back, whichever is closer to the desired index), this method will have the same runtime
    # regardless of how many or how few items there are in the linked list.
    
    if len(self.__list) == 0:
      return None
    returned = self.__list.remove_element_at(len(self.__list) - 1)
    return returned

  def peek_back(self):
    """Returns the item at the back of the deque"""

    # PERFORMANCE:
    # This method is constant O(1). This method calls get_element_at from the Linked_List file, which
    # runs in linear time, though because the index that's being removed is the last index, and because the
    # __position_before_index method has been optimized (making it start iterating from the front or back,
    # whichever is closer to the desired index), this method will have the same runtime regardless of how
    # many or how few items there are inside of the linked list.

    if len(self.__list) == 0:
      return None

    return self.__list.get_element_at(len(self.__list) - 1)

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
