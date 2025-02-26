from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    """Returns the string representation of the stack"""

    # PERFORMANCE:
    # This method is linear O(n), because this function just calls the __str__ method of the deque, and
    # the performance of the __str__ call of both an array based and linked list based deque is O(n),
    # so the worst case will always be O(n) regardless of which (LL or Array based) deque is used.

    return str(self.__dq)

  def __len__(self):
    """Returns the integer representation of the amount of items in the stack"""

    # PERFORMANCE:
    # This method is constant O(1), because this function just calls the __len__ method of the deque, and
    # the performance of the __len__ call of both an array based and linked list based deque is O(1), and
    # therefore the worst case will always be O(1) regardless of which deque is used.

    return len(self.__dq)

  def push(self, val):
    """Adds an item at the top of the stack"""

    # PERFORMANCE:
    # This method is linear O(n), because the push_front method of an array based deque is O(n) and the push_front
    # method of a linked list based deque is O(1), and as O(n) > O(1), this method is O(n) in the worst case scenario.

    self.__dq.push_front(val)

  def pop(self):
    """Removes the item at the top of the stack and returns its value"""

    # PERFORMANCE:
    # This method is constant O(1), because the pop_front method of both an array based and linked list based deque
    # is O(1), meaning that the worst case performance will be O(1) regardless of whether a linked list or array based
    # deque is used.

    returned = self.__dq.pop_front()
    return returned

  def peek(self):
    """Returns the value of the item at the top of the stack"""

    # PERFORMANCE:
    # This method is constant O(1), because the peek_front method of both an array based and linked list based deque
    # is O(1), which means that the worst case performance will be O(1) regardless of which type of deque is used.

    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
