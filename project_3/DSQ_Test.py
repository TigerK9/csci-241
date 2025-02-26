import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
    
    def setUp(self):
        self.__deque = get_deque()
        self.__stack = Stack()
        self.__queue = Queue()
    
    # *~=~=~* Start deque tests *~=~=~*
        
    def test_deque_empty_string(self):
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_empty_push_front_string(self):
        self.__deque.push_front(1)
        self.assertEqual("[ 1 ]", str(self.__deque))

    def test_deque_empty_push_back_string(self):
        self.__deque.push_back(1)
        self.assertEqual("[ 1 ]", str(self.__deque))

    def test_deque_push_front_with_one_string(self):
        self.__deque.push_front(2)
        self.__deque.push_front(1)
        self.assertEqual("[ 1, 2 ]", str(self.__deque))

    def test_deque_push_front_with_two_string(self):
        self.__deque.push_front("one")
        self.__deque.push_front("two")
        self.__deque.push_front("three")
        self.assertEqual("[ three, two, one ]", str(self.__deque))

    def test_deque_push_front_with_four_string(self):
        self.__deque.push_front("one")
        self.__deque.push_front("two")
        self.__deque.push_front("three")
        self.__deque.push_front("four")
        self.__deque.push_front("five")
        self.assertEqual("[ five, four, three, two, one ]", str(self.__deque))

    def test_deque_push_front_with_eight_string(self):
        self.__deque.push_front("one")
        self.__deque.push_front("two")
        self.__deque.push_front("three")
        self.__deque.push_front("four")
        self.__deque.push_front("five")
        self.__deque.push_front("six")
        self.__deque.push_front("seven")
        self.__deque.push_front("eight")
        self.__deque.push_front("nine")
        self.assertEqual("[ nine, eight, seven, six, five, four, three, two, one ]", str(self.__deque))

    def test_deque_push_back_with_one_string(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual("[ 1, 2 ]", str(self.__deque))

    def test_deque_push_back_with_two_string(self):
        self.__deque.push_back("one")
        self.__deque.push_back("two")
        self.__deque.push_back("three")
        self.assertEqual("[ one, two, three ]", str(self.__deque))

    def test_deque_push_back_with_four_string(self):
        self.__deque.push_back("one")
        self.__deque.push_back("two")
        self.__deque.push_back("three")
        self.__deque.push_back("four")
        self.__deque.push_back("five")
        self.assertEqual("[ one, two, three, four, five ]", str(self.__deque))

    def test_deque_push_back_with_eight_string(self):
        self.__deque.push_back("one")
        self.__deque.push_back("two")
        self.__deque.push_back("three")
        self.__deque.push_back("four")
        self.__deque.push_back("five")
        self.__deque.push_back("six")
        self.__deque.push_back("seven")
        self.__deque.push_back("eight")
        self.__deque.push_back("nine")
        self.assertEqual("[ one, two, three, four, five, six, seven, eight, nine ]", str(self.__deque))

    def test_deque_empty_deque_length(self):
        self.assertEqual(0, len(self.__deque))

    def test_deque_push_front_one_length(self):
        self.__deque.push_front(1)
        self.assertEqual(1, len(self.__deque))
    
    def test_deque_push_front_two_length(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, len(self.__deque))

    def test_deque_push_front_three_length(self):
        for x in range(3):
            self.__deque.push_front(x)
        self.assertEqual(3, len(self.__deque))

    def test_deque_push_back_one_length(self):
        self.__deque.push_back(1)
        self.assertEqual(1, len(self.__deque))

    def test_deque_push_back_one_length(self):
        self.__deque.push_back(1)
        self.assertEqual(1, len(self.__deque))

    def test_deque_push_back_two_length(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2, len(self.__deque))

    def test_deque_push_back_three_length(self):
        for x in range(3):
            self.__deque.push_back(x)
        self.assertEqual(3, len(self.__deque))

    def test_deque_pop_front_with_one_string(self):
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_pop_front_with_two_string(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_front()
        self.assertEqual("[ 1 ]", str(self.__deque))

    def test_deque_pop_front_with_three_string(self):
        for x in range(3):
            self.__deque.push_front(x)
        self.__deque.pop_front()
        self.assertEqual("[ 1, 0 ]", str(self.__deque))

    def test_deque_pop_front_with_five_string(self):
        for x in range(5):
            self.__deque.push_front(x)
        self.__deque.pop_front()
        self.assertEqual("[ 3, 2, 1, 0 ]", str(self.__deque))

    def test_deque_pop_front_return_value_int(self):
        self.__deque.push_front(3)
        self.__deque.push_front(2)
        self.__deque.push_front(1)
        returned = self.__deque.pop_front()
        self.assertEqual(1,returned)

    def test_deque_pop_front_return_value_str(self):
        self.__deque.push_front("3")
        self.__deque.push_front("2")
        self.__deque.push_front("1")
        returned = self.__deque.pop_front()
        self.assertEqual("1",returned)

    def test_deque_pop_front_return_value_none(self):
        self.__deque.push_front(None)
        self.__deque.push_front(None)
        self.__deque.push_front(None)
        returned = self.__deque.pop_front()
        self.assertEqual(None,returned)

    def test_deque_pop_back_with_one_string(self):
        self.__deque.push_front(1)
        self.__deque.pop_back()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_pop_back_with_two_string(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.pop_back()
        self.assertEqual("[ 1 ]", str(self.__deque))

    def test_deque_pop_back_with_three_string(self):
        for x in range(3):
            self.__deque.push_back(x)
        self.__deque.pop_back()
        self.assertEqual("[ 0, 1 ]", str(self.__deque))

    def test_deque_pop_back_with_five_string(self):
        for x in range(5):
            self.__deque.push_back(x)
        self.__deque.pop_back()
        self.assertEqual("[ 0, 1, 2, 3 ]", str(self.__deque))
    
    def test_deque_pop_front_with_one_length(self):
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual(0, len(self.__deque))

    def test_deque_pop_front_with_two_length(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.pop_front()
        self.assertEqual(1, len(self.__deque))

    def test_deque_pop_front_with_three_length(self):
        for x in range(3):
            self.__deque.push_front(x)
        self.__deque.pop_front()
        self.assertEqual(2, len(self.__deque))

    def test_deque_pop_front_with_five_length(self):
        for x in range(5):
            self.__deque.push_front(x)
        self.__deque.pop_front()
        self.assertEqual(4, len(self.__deque))

    def test_deque_pop_back_with_one_length(self):
        self.__deque.push_back(1)
        self.__deque.pop_back()
        self.assertEqual(0, len(self.__deque))

    def test_deque_pop_back_with_two_length(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.pop_back()
        self.assertEqual(1, len(self.__deque))

    def test_deque_pop_back_with_three_length(self):
        for x in range(3):
            self.__deque.push_back(x)
        self.__deque.pop_back()
        self.assertEqual(2, len(self.__deque))

    def test_deque_pop_back_with_five_length(self):
        for x in range(5):
            self.__deque.push_back(x)
        self.__deque.pop_back()
        self.assertEqual(4, len(self.__deque))

    def test_deque_pop_back_return_value_int(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        returned = self.__deque.pop_back()
        self.assertEqual(3,returned)

    def test_deque_pop_back_return_value_str(self):
        self.__deque.push_back("1")
        self.__deque.push_back("2")
        self.__deque.push_back("3")
        returned = self.__deque.pop_back()
        self.assertEqual("3",returned)

    def test_deque_pop_back_return_value_none(self):
        self.__deque.push_back(None)
        self.__deque.push_back(None)
        self.__deque.push_back(None)
        returned = self.__deque.pop_back()
        self.assertEqual(None,returned)

    def test_deque_pop_front_with_five_until_empty_string(self):
        for x in range(5):
            self.__deque.push_back(x)
        for _ in range(5):
            self.__deque.pop_front()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_pop_back_with_five_until_empty_string(self):
        for x in range(5):
            self.__deque.push_front(x)
        for _ in range(5):
            self.__deque.pop_back()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_pop_front_with_five_until_empty_length(self):
        for x in range(5):
            self.__deque.push_back(x)
        for _ in range(5):
            self.__deque.pop_front()
        self.assertEqual(0, len(self.__deque))

    def test_deque_pop_back_with_five_until_empty_length(self):
        for x in range(5):
            self.__deque.push_front(x)
        for _ in range(5):
            self.__deque.pop_back()
        self.assertEqual(0, len(self.__deque))

    def test_deque_alternating_push_types_for_two_string(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.assertEqual("[ 1, 2 ]", str(self.__deque))

    def test_deque_alternating_push_types_for_five_string(self):
        self.__deque.push_front(3)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_back(5)
        self.__deque.push_front(1)
        self.assertEqual("[ 1, 2, 3, 4, 5 ]", str(self.__deque))

    def test_deque_alternating_push_types_for_two_length(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.assertEqual(2, len(self.__deque))

    def test_deque_alternating_push_types_for_five_length(self):
        self.__deque.push_front(3)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_back(5)
        self.__deque.push_front(1)
        self.assertEqual(5, len(self.__deque))

    def test_deque_alternating_push_types_for_two_then_pop_front_string(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.__deque.pop_front()
        self.assertEqual("[ 2 ]", str(self.__deque))

    def test_deque_alternating_push_types_for_two_then_pop_back_string(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.__deque.pop_back()
        self.assertEqual("[ 1 ]", str(self.__deque))

    def test_deque_alternating_push_types_for_five_then_pop_front_string(self):
        self.__deque.push_front(3)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_back(5)
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual("[ 2, 3, 4, 5 ]", str(self.__deque))

    def test_deque_alternating_push_types_for_five_then_pop_back_string(self):
        self.__deque.push_front(3)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_back(5)
        self.__deque.push_front(1)
        self.__deque.pop_back()
        self.assertEqual("[ 1, 2, 3, 4 ]", str(self.__deque))

    def test_deque_push_front_one_none_string(self):
        self.__deque.push_front(None)
        self.assertEqual("[ None ]", str(self.__deque))

    def test_deque_push_front_three_none_string(self):
        for _ in range(3):
            self.__deque.push_front(None)
        self.assertEqual("[ None, None, None ]", str(self.__deque))

    def test_deque_push_front_five_none_string(self):
        for _ in range(5):
            self.__deque.push_front(None)
        self.assertEqual("[ None, None, None, None, None ]", str(self.__deque))

    def test_deque_push_front_one_none_length(self):
        self.__deque.push_front(None)
        self.assertEqual(1, len(self.__deque))

    def test_deque_push_front_three_none_length(self):
        for _ in range(3):
            self.__deque.push_front(None)
        self.assertEqual(3, len(self.__deque))

    def test_deque_push_front_five_none_length(self):
        for _ in range(5):
            self.__deque.push_front(None)
        self.assertEqual(5, len(self.__deque))

    def test_deque_push_back_one_none_string(self):
        self.__deque.push_back(None)
        self.assertEqual("[ None ]", str(self.__deque))

    def test_deque_push_back_three_none_string(self):
        for _ in range(3):
            self.__deque.push_back(None)
        self.assertEqual("[ None, None, None ]", str(self.__deque))

    def test_deque_push_back_five_none_string(self):
        for _ in range(5):
            self.__deque.push_back(None)
        self.assertEqual("[ None, None, None, None, None ]", str(self.__deque))

    def test_deque_push_back_one_none_length(self):
        self.__deque.push_back(None)
        self.assertEqual(1, len(self.__deque))

    def test_deque_push_back_three_none_length(self):
        for _ in range(3):
            self.__deque.push_back(None)
        self.assertEqual(3, len(self.__deque))

    def test_deque_push_back_five_none_length(self):
        for _ in range(5):
            self.__deque.push_back(None)
        self.assertEqual(5, len(self.__deque))

    def test_deque_none_at_one_of_four(self):
        self.__deque.push_back(None)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual("[ None, 2, 3, 4 ]", str(self.__deque))

    def test_deque_none_at_two_of_four(self):
        self.__deque.push_back(1)
        self.__deque.push_back(None)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.assertEqual("[ 1, None, 3, 4 ]", str(self.__deque))

    def test_deque_none_at_three_of_four(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(None)
        self.__deque.push_back(4)
        self.assertEqual("[ 1, 2, None, 4 ]", str(self.__deque))

    def test_deque_none_at_four_of_four(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(None)
        self.assertEqual("[ 1, 2, 3, None ]", str(self.__deque))

    def test_deque_peek_front_with_one_element(self):
        self.__deque.push_front("Wimberley")
        returned = self.__deque.peek_front()
        self.assertEqual(returned, "Wimberley")

    def test_deque_peek_front_with_one_element_length(self):
        self.__deque.push_front("Wimberley")
        self.__deque.peek_front()
        self.assertEqual(1,len(self.__deque))

    def test_deque_peek_front_with_one_element_string(self):
        self.__deque.push_front("Wimberley")
        self.__deque.peek_front()
        self.assertEqual("[ Wimberley ]", str(self.__deque))

    def test_deque_peek_front_with_two_elements(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        returned = self.__deque.peek_front()
        self.assertEqual(returned, "Wimberley")

    def test_deque_peek_front_with_two_elements_length(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        self.__deque.peek_front()
        self.assertEqual(2,len(self.__deque))

    def test_deque_peek_front_with_two_elements_string(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        self.__deque.peek_front()
        self.assertEqual("[ Wimberley, Texas ]", str(self.__deque))

    def test_deque_peek_front_with_three_elements(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        self.__deque.push_back(78676)
        returned = self.__deque.peek_front()
        self.assertEqual(returned, "Wimberley")

    def test_deque_peek_front_with_three_elements_length(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        self.__deque.push_back(78676)
        self.__deque.peek_front()
        self.assertEqual(3,len(self.__deque))

    def test_deque_peek_front_with_three_elements_string(self):
        self.__deque.push_front("Wimberley")
        self.__deque.push_back("Texas")
        self.__deque.push_back(78676)
        self.__deque.peek_front()
        self.assertEqual("[ Wimberley, Texas, 78676 ]", str(self.__deque))

    def test_deque_peek_back_with_one_element(self):
        self.__deque.push_front("William")
        returned = self.__deque.peek_back()
        self.assertEqual(returned, "William")

    def test_deque_peek_back_with_one_element_length(self):
        self.__deque.push_front("William")
        self.__deque.peek_back()
        self.assertEqual(1, len(self.__deque))

    def test_deque_peek_back_with_one_element_string(self):
        self.__deque.push_front("William")
        self.__deque.peek_back()
        self.assertEqual("[ William ]", str(self.__deque))

    def test_deque_peek_back_with_two_elements(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        returned = self.__deque.peek_back()
        self.assertEqual(returned, "&")

    def test_deque_peek_back_with_two_elements_length(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        self.__deque.peek_back()
        self.assertEqual(2, len(self.__deque))

    def test_deque_peek_back_with_two_elements_string(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        self.__deque.peek_back()
        self.assertEqual("[ William, & ]", str(self.__deque))

    def test_deque_peek_back_with_three_elements(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        self.__deque.push_back("Mary")
        returned = self.__deque.peek_back()
        self.assertEqual(returned, "Mary")

    def test_deque_peek_back_with_three_elements_length(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        self.__deque.push_back("Mary")
        self.__deque.peek_back()
        self.assertEqual(3, len(self.__deque))

    def test_deque_peek_back_with_three_elements_string(self):
        self.__deque.push_front("William")
        self.__deque.push_back("&")
        self.__deque.push_back("Mary")
        self.__deque.peek_back()
        self.assertEqual("[ William, &, Mary ]", str(self.__deque))

    def test_deque_push_front_and_back_ten_pop_until_empty_string(self):
        for _ in range(5):
            self.__deque.push_front(0)
            self.__deque.push_back("back")
        for _ in range(5):
            self.__deque.pop_front()
            self.__deque.pop_back()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_push_front_and_back_ten_pop_until_empty_length(self):
        for _ in range(5):
            self.__deque.push_front(0)
            self.__deque.push_back("back")
        for _ in range(5):
            self.__deque.pop_front()
            self.__deque.pop_back()
        self.assertEqual(0, len(self.__deque))

    def test_deque_push_front_pop_back_alternating_five_times_string(self):
        for _ in range(5):
            self.__deque.push_front(1)
            self.__deque.pop_back()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_push_front_pop_back_alternating_five_times_length(self):
        for _ in range(5):
            self.__deque.push_front(1)
            self.__deque.pop_back()
        self.assertEqual(0, len(self.__deque))

    def test_deque_push_back_pop_front_alternating_five_times_string(self):
        for _ in range(5):
            self.__deque.push_back(1)
            self.__deque.pop_front()
        self.assertEqual("[ ]", str(self.__deque))

    def test_deque_push_back_pop_front_alternating_five_times_length(self):
        for _ in range(5):
            self.__deque.push_back(1)
            self.__deque.pop_front()
        self.assertEqual(0, len(self.__deque))

    def test_deque_pop_front_none_of_three_string(self):
        self.__deque.push_back(None)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_front()
        self.assertEqual("[ 2, 3 ]", str(self.__deque))

    def test_deque_pop_front_none_of_three_length(self):
        self.__deque.push_back(None)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_front()
        self.assertEqual(2, len(self.__deque))

    def test_deque_pop_back_none_of_three_string(self):
        self.__deque.push_front(None)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.assertEqual("[ 3, 2 ]", str(self.__deque))

    def test_deque_pop_back_none_of_three_length(self):
        self.__deque.push_front(None)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.assertEqual(2, len(self.__deque))
        
    def test_deque_peek_none(self):
        self.__deque.push_front(None)
        returned = self.__deque.peek_front()
        self.assertEqual(returned, None)

    def test_deque_peek_non_string(self):
        self.__deque.push_front(None)
        self.__deque.peek_front()
        self.assertEqual("[ None ]", str(self.__deque))

    def test_deque_peek_non_length(self):
        self.__deque.push_front(None)
        self.__deque.peek_front()
        self.assertEqual(1, len(self.__deque))

    def test_deque_circularity_with_four_elements_front(self):
        self.__deque.push_front(999)
        self.__deque.push_front(888)
        self.__deque.push_front(777)
        self.__deque.push_front(666)
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual("[ 888, 999, 1, 2 ]", str(self.__deque))

    def test_deque_circularity_with_four_elements_back(self):
        self.__deque.push_back(666)
        self.__deque.push_back(777)
        self.__deque.push_back(888)
        self.__deque.push_back(999)
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.__deque.push_front(2)
        self.__deque.push_front(1)
        self.assertEqual("[ 1, 2, 666, 777 ]", str(self.__deque))


    # TEST WRAP AROUND : ADD ELEMENTS THEN REMOVE FRONT, ADD BACK, AND SEE IF WRAPPED AROUND IT'S STILL FORMATTED CORRECTLY

    # *~=~=~* End deque tests *~=~=~*



    # *~=~=~* Start stack tests *~=~=~*

    def test_stack_empty_string(self):
        self.assertEqual("[ ]", str(self.__stack))

    def test_stack_empty_length(self):
        self.assertEqual(0, len(self.__stack))

    def test_stack_push_one_string(self):
        self.__stack.push(1)
        self.assertEqual("[ 1 ]", str(self.__stack))

    def test_stack_push_one_length(self):
        self.__stack.push(1)
        self.assertEqual(1, len(self.__stack))

    def test_stack_push_three_string(self):
        self.__stack.push("one")
        self.__stack.push("two")
        self.__stack.push("three")
        self.assertEqual("[ three, two, one ]", str(self.__stack))

    def test_stack_push_three_length(self):
        self.__stack.push("one")
        self.__stack.push("two")
        self.__stack.push("three")
        self.assertEqual(3, len(self.__stack))

    def test_stack_push_one_none_string(self):
        self.__stack.push(None)
        self.assertEqual("[ None ]", str(self.__stack))

    def test_stack_push_one_none_length(self):
        self.__stack.push(None)
        self.assertEqual(1, len(self.__stack))

    def test_stack_push_three_none_string(self):
        for _ in range(3):
            self.__stack.push(None)
        self.assertEqual("[ None, None, None ]", str(self.__stack))

    def test_stack_push_three_none_length(self):
        for _ in range(3):
            self.__stack.push(None)
        self.assertEqual(3, len(self.__stack))

    def test_stack_none_at_one_of_three_string(self):
        self.__stack.push("last")
        self.__stack.push(2)
        self.__stack.push(None)
        self.assertEqual("[ None, 2, last ]", str(self.__stack))

    def test_stack_none_at_one_of_three_length(self):
        self.__stack.push("last")
        self.__stack.push(2)
        self.__stack.push(None)
        self.assertEqual(3, len(self.__stack))

    def test_stack_none_at_two_of_three_string(self):
        self.__stack.push("last")
        self.__stack.push(None)
        self.__stack.push(1)
        self.assertEqual("[ 1, None, last ]", str(self.__stack))

    def test_stack_none_at_two_of_three_length(self):
        self.__stack.push("last")
        self.__stack.push(None)
        self.__stack.push(1)
        self.assertEqual(3, len(self.__stack))

    def test_stack_none_at_three_of_three_string(self):
        self.__stack.push(None)
        self.__stack.push("middle")
        self.__stack.push(1)
        self.assertEqual("[ 1, middle, None ]", str(self.__stack))

    def test_stack_none_at_three_of_three_length(self):
        self.__stack.push(None)
        self.__stack.push("middle")
        self.__stack.push(1)
        self.assertEqual(3, len(self.__stack))

    def test_stack_pop_one_string(self):
        self.__stack.push(1)
        self.__stack.pop()
        self.assertEqual("[ ]", str(self.__stack))

    def test_stack_pop_one_length(self):
        self.__stack.push(1)
        self.__stack.pop()
        self.assertEqual(0, len(self.__stack))

    def test_stack_pop_one_of_three_string(self):
        self.__stack.push(1)
        self.__stack.push("two")
        self.__stack.push(333)
        self.__stack.pop()
        self.assertEqual("[ two, 1 ]", str(self.__stack))

    def test_stack_pop_one_of_three_length(self):
        self.__stack.push(1)
        self.__stack.push("two")
        self.__stack.push(333)
        self.__stack.pop()
        self.assertEqual(2, len(self.__stack))

    def test_stack_pop_two_of_three_string(self):
        self.__stack.push(1)
        self.__stack.push("two")
        self.__stack.push(333)
        self.__stack.pop()
        self.__stack.pop()
        self.assertEqual("[ 1 ]", str(self.__stack))

    def test_stack_pop_two_of_three_length(self):
        self.__stack.push(1)
        self.__stack.push("two")
        self.__stack.push(333)
        self.__stack.pop()
        self.__stack.pop()
        self.assertEqual(1, len(self.__stack))
    
    def test_stack_pop_none_string(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(None)
        self.__stack.pop()
        self.assertEqual("[ 2, 1 ]", str(self.__stack))

    def test_stack_pop_none_length(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(None)
        self.__stack.pop()
        self.assertEqual(2, len(self.__stack))

    def test_stack_pop_three_times_until_empty_string(self):
        for _ in range(3):
            self.__stack.push("x")
        for _ in range(3):
            self.__stack.pop()
        self.assertEqual("[ ]", str(self.__stack))

    def test_stack_pop_three_times_until_empty_length(self):
        for _ in range(3):
            self.__stack.push("x")
        for _ in range(3):
            self.__stack.pop()
        self.assertEqual(0, len(self.__stack))

    def test_stack_alternate_push_and_pop_five_times_string(self):
        for _ in range(3):
            self.__stack.push(1)
            self.__stack.pop()
        self.assertEqual("[ ]", str(self.__stack))

    def test_stack_alternate_push_and_pop_five_times_length(self):
        for _ in range(3):
            self.__stack.push(1)
            self.__stack.pop()
        self.assertEqual(0, len(self.__stack))

    def test_stack_peek_one(self):
        self.__stack.push(1)
        returned = self.__stack.peek()
        self.assertEqual(returned, 1)

    def test_stack_peek_one_string(self):
        self.__stack.push(1)
        self.__stack.peek()
        self.assertEqual("[ 1 ]", str(self.__stack))

    def test_stack_peek_one_length(self):
        self.__stack.push(1)
        self.__stack.peek()
        self.assertEqual(1, len(self.__stack))

    def test_stack_peek_one_of_three(self):
        for x in range(3):
            self.__stack.push(x)
        returned = self.__stack.peek()
        self.assertEqual(returned, 2)

    def test_stack_peek_one_of_three_string(self):
        for x in range(3):
            self.__stack.push(x)
        self.__stack.peek()
        self.assertEqual("[ 2, 1, 0 ]", str(self.__stack))

    def test_stack_peek_one_of_three_length(self):
        for x in range(3):
            self.__stack.push(x)
        self.__stack.peek()
        self.assertEqual(3, len(self.__stack))

    def test_stack_peek_none(self):
        self.__stack.push(None)
        returned = self.__stack.peek()
        self.assertEqual(returned, None)

    def test_stack_peek_none_string(self):
        self.__stack.push(None)
        self.__stack.peek()
        self.assertEqual("[ None ]", str(self.__stack))

    def test_stack_peek_none_length(self):
        self.__stack.push(None)
        self.__stack.peek()
        self.assertEqual(1, len(self.__stack))

    # *~=~=~* End stack tests *~=~=~*
        


    # *~=~=~* Start queue tests *~=~=~*
        
    def test_queue_empty_string(self):
        self.assertEqual("[ ]", str(self.__queue))

    def test_queue_empty_length(self):
        self.assertEqual(0, len(self.__queue))

    def test_queue_enqueue_one_string(self):
        self.__queue.enqueue(1)
        self.assertEqual("[ 1 ]", str(self.__queue))

    def test_queue_enqueue_one_length(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, len(self.__queue))

    def test_queue_enqueue_three_string(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue("two")
        self.__queue.enqueue(3)
        self.assertEqual("[ 1, two, 3 ]", str(self.__queue))

    def test_queue_enqueue_three_length(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue("two")
        self.__queue.enqueue(3)
        self.assertEqual(3, len(self.__queue))

    def test_queue_enqueue_one_none_string(self):
        self.__queue.enqueue(None)
        self.assertEqual("[ None ]", str(self.__queue))

    def test_queue_enqueue_one_none_length(self):
        self.__queue.enqueue(None)
        self.assertEqual(1, len(self.__queue))

    def test_queue_enqueue_three_none_string(self):
        for _ in range(3):
            self.__queue.enqueue(None)
        self.assertEqual("[ None, None, None ]", str(self.__queue))

    def test_queue_enqueue_three_none_length(self):
        for _ in range(3):
            self.__queue.enqueue(None)
        self.assertEqual(3, len(self.__queue))

    def test_queue_dequeue_one_string(self):
        self.__queue.enqueue(1)
        self.__queue.dequeue()
        self.assertEqual("[ ]", str(self.__queue))

    def test_queue_dequeue_one_length(self):
        self.__queue.enqueue(1)
        self.__queue.dequeue()
        self.assertEqual(0, len(self.__queue))

    def test_queue_dequeue_one_of_three_string(self):
        for x in range(3):
            self.__queue.enqueue(x)
        self.__queue.dequeue()
        self.assertEqual("[ 1, 2 ]", str(self.__queue))

    def test_queue_dequeue_one_of_three_length(self):
        for x in range(3):
            self.__queue.enqueue(x)
        self.__queue.dequeue()
        self.assertEqual(2, len(self.__queue))

    def test_queue_dequeue_two_of_three_string(self):
        for x in range(3):
            self.__queue.enqueue(x)
        self.__queue.dequeue()
        self.__queue.dequeue()
        self.assertEqual("[ 2 ]", str(self.__queue))

    def test_queue_dequeue_two_of_three_length(self):
        for x in range(3):
            self.__queue.enqueue(x)
        self.__queue.dequeue()
        self.__queue.dequeue()
        self.assertEqual(1, len(self.__queue))

    def test_queue_dequeue_three_of_three_string(self):
        for x in range(3):
            self.__queue.enqueue(x)
        for _ in range(3):
            self.__queue.dequeue()
        self.assertEqual("[ ]", str(self.__queue))

    def test_queue_dequeue_three_of_three_length(self):
        for x in range(3):
            self.__queue.enqueue(x)
        for _ in range(3):
            self.__queue.dequeue()
        self.assertEqual(0, len(self.__queue))

    def test_queue_dequeue_return_str(self):
        self.__queue.enqueue("1")
        self.__queue.enqueue("2")
        self.__queue.enqueue("3")
        returned = self.__queue.dequeue()
        self.assertEqual(returned, "1")

    def test_queue_dequeue_return_int(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        returned = self.__queue.dequeue()
        self.assertEqual(returned, 1)

    def test_queue_dequeue_return_none(self):
        self.__queue.enqueue(None)
        self.__queue.enqueue(2)
        self.__queue.enqueue("3")
        returned = self.__queue.dequeue()
        self.assertEqual(returned, None)

    def test_queue_enqueue_none_at_one_of_three_string(self):
        self.__queue.enqueue(None)
        self.__queue.enqueue(2)
        self.__queue.enqueue("three")
        self.assertEqual("[ None, 2, three ]", str(self.__queue))

    def test_queue_enqueue_none_at_one_of_three_length(self):
        self.__queue.enqueue(None)
        self.__queue.enqueue(2)
        self.__queue.enqueue("three")
        self.assertEqual(3, len(self.__queue))

    def test_queue_enqueue_none_at_two_of_three_string(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(None)
        self.__queue.enqueue("three")
        self.assertEqual("[ 1, None, three ]", str(self.__queue))

    def test_queue_enqueue_none_at_two_of_three_length(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(None)
        self.__queue.enqueue("three")
        self.assertEqual(3, len(self.__queue))

    def test_queue_enqueue_none_at_three_of_three_string(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue("two")
        self.__queue.enqueue(None)
        self.assertEqual("[ 1, two, None ]", str(self.__queue))

    def test_queue_enqueue_none_at_three_of_three_length(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue("two")
        self.__queue.enqueue(None)
        self.assertEqual(3, len(self.__queue))

    def test_queue_peek_one_of_one(self):
        self.__queue.enqueue("Wimberley")
        returned = self.__queue.peek()
        self.assertEqual(returned, "Wimberley")

    def test_queue_peek_one_of_one_string(self):
        self.__queue.enqueue("Wimberley")
        self.__queue.peek()
        self.assertEqual("[ Wimberley ]", str(self.__queue))

    def test_queue_peek_one_of_one_length(self):
        self.__queue.enqueue("Wimberley")
        self.__queue.peek()
        self.assertEqual(1, len(self.__queue))

    def test_queue_peek_one_of_three(self):
        self.__queue.enqueue("one")
        self.__queue.enqueue(2)
        self.__queue.enqueue("three")
        returned = self.__queue.peek()
        self.assertEqual("one", returned)

    def test_queue_peek_one_of_three_string(self):
        self.__queue.enqueue("one")
        self.__queue.enqueue(2)
        self.__queue.enqueue("three")
        self.__queue.peek()
        self.assertEqual("[ one, 2, three ]", str(self.__queue))

    def test_queue_peek_one_of_three_length(self):
        self.__queue.enqueue("one")
        self.__queue.enqueue(2)
        self.__queue.enqueue("three")
        self.__queue.peek()
        self.assertEqual(3, len(self.__queue))

    def test_queue_peek_none(self):
        self.__queue.enqueue(None)
        returned = self.__queue.peek()
        self.assertEqual(returned, None)

    def test_queue_peek_none_string(self):
        self.__queue.enqueue(None)
        self.__queue.peek()
        self.assertEqual("[ None ]", str(self.__queue))

    def test_queue_peek_none_length(self):
        self.__queue.enqueue(None)
        self.__queue.peek()
        self.assertEqual(1, len(self.__queue))

    # *~=~=~* End queue tests *~=~=~*


    # ADD DEQUEUE RETURN VALUE TESTS
    # ADD RETURN CORRECT VARIABLE TYPE TEST FOR DEQUE: 7 == 7, but 7 != '7'



if __name__ == '__main__':
    unittest.main()

