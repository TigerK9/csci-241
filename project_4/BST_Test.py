from contextlib import AbstractContextManager
from typing import Any
import unittest
from Binary_Search_Tree import Binary_Search_Tree

class DSQTester(unittest.TestCase):
    
    def setUp(self):
        self.bst = Binary_Search_Tree()

    # Empty:
    # seperate test to make sure pre-order, in-order, post work
    def test_empty_height(self):
        self.assertEqual(self.bst.get_height(), 0)

    def test_empty_string(self):
        self.assertEqual(str(self.bst), "[ ]")

    def test_empty_string_in_order(self):
        self.assertEqual(self.bst.in_order(), "[ ]")

    def test_empty_string_pre_order(self):
        self.assertEqual(self.bst.pre_order(), "[ ]")

    def test_empty_string_post_order(self):
        self.assertEqual(self.bst.post_order(), "[ ]")

    # One element
    def test_one_element_height(self):
        self.bst.insert_element(1)
        self.assertEqual(self.bst.get_height(), 1)

    def test_one_element_string(self):
        self.bst.insert_element(1)
        self.assertEqual(str(self.bst), "[ 1 ]")

    def test_one_element_in_order(self):
        self.bst.insert_element(1)
        self.assertEqual(self.bst.in_order(), "[ 1 ]")

    def test_one_element_pre_order(self):
        self.bst.insert_element(1)
        self.assertEqual(self.bst.pre_order(), "[ 1 ]")

    def test_one_element_post_order(self):
        self.bst.insert_element(1)
        self.assertEqual(self.bst.post_order(), "[ 1 ]")

    # Two elements
    def test_two_elements_height(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.assertEqual(self.bst.get_height(), 2)

    def test_two_elements_string(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.assertEqual(str(self.bst), "[ 1, 2 ]")

    def test_two_elements_in_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.assertEqual(self.bst.in_order(), "[ 1, 2 ]")

    def test_two_elements_pre_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.assertEqual(self.bst.pre_order(), "[ 1, 2 ]")

    def test_two_elements_post_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.assertEqual(self.bst.post_order(), "[ 2, 1 ]")

    # Three elements, perfect tree
    def test_three_elements_perfect_tree_height(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.get_height(), 2)

    def test_three_elements_perfect_tree_string(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        self.assertEqual(str(self.bst), "[ 1, 2, 3 ]")

    def test_three_elements_perfect_tree_in_order(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.in_order(), "[ 1, 2, 3 ]")

    def test_three_elements_perfect_tree_pre_order(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.pre_order(), "[ 2, 1, 3 ]")

    def test_three_elements_perfect_tree_post_order(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.post_order(), "[ 1, 3, 2 ]")

    # Empty after removing one node
    def test_empty_after_removal_of_one_height(self):
        self.bst.insert_element(1)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.get_height(), 0)

    def test_empty_after_removal_of_one_string(self):
        self.bst.insert_element(1)
        self.bst.remove_element(1)
        self.assertEqual(str(self.bst), "[ ]")

    def test_empty_after_removal_of_one_in_order(self):
        self.bst.insert_element(1)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.in_order(), "[ ]")

    def test_empty_after_removal_of_one_pre_order(self):
        self.bst.insert_element(1)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.pre_order(), "[ ]")

    def test_empty_after_removal_of_one_post_order(self):
        self.bst.insert_element(1)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.post_order(), "[ ]")

    # tree after removing left leaf, starting with perfect tree of three elements
    def test_tree_remove_left_leaf_of_perfect_height(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(22)
        self.assertEqual(self.bst.get_height(), 2)

    def test_tree_remove_left_leaf_of_perfect_string(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(22)
        self.assertEqual(str(self.bst), "[ 33, 44 ]")

    def test_tree_remove_left_leaf_of_perfect_in_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(22)
        self.assertEqual(self.bst.in_order(), "[ 33, 44 ]")

    def test_tree_remove_left_leaf_of_perfect_pre_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(22)
        self.assertEqual(self.bst.pre_order(), "[ 33, 44 ]")

    def test_tree_remove_left_leaf_of_perfect_post_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(22)
        self.assertEqual(self.bst.post_order(), "[ 44, 33 ]")

    # tree after removing right leaf, starting with perfect tree of three elements
    def test_tree_remove_right_leaf_of_perfect_height(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(44)
        self.assertEqual(self.bst.get_height(), 2)

    def test_tree_remove_right_leaf_of_perfect_tree_string(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(44)
        self.assertEqual(str(self.bst), "[ 22, 33 ]")

    def test_tree_remove_right_leaf_of_perfect_tree_traversals(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(44)
        self.assertEqual(self.bst.in_order(), "[ 22, 33 ]")
        self.assertEqual(self.bst.pre_order(), "[ 33, 22 ]")
        self.assertEqual(self.bst.post_order(), "[ 22, 33 ]")

    # tree after removing parent node, starting with perfect tree of three elements
    def test_tree_remove_parent_node_of_perfect_height(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(33)
        self.assertEqual(self.bst.get_height(), 2)

    def test_tree_remove_parent_node_of_perfect_string(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(33)
        self.assertEqual(str(self.bst), "[ 22, 44 ]")

    def test_tree_remove_parent_node_of_perfect_in_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(33)
        self.assertEqual(self.bst.in_order(), "[ 22, 44 ]")

    def test_tree_remove_parent_node_of_perfect_pre_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(33)
        self.assertEqual(self.bst.pre_order(), "[ 44, 22 ]")

    def test_tree_remove_parent_node_of_perfect_post_order(self):
        self.bst.insert_element(33)
        self.bst.insert_element(22)
        self.bst.insert_element(44)
        self.bst.remove_element(33)
        self.assertEqual(self.bst.post_order(), "[ 22, 44 ]")

    def test_insertion_of_same_value(self):
        self.bst.insert_element(1)
        try:
            self.bst.insert_element(1)
        except ValueError:
            self.assertEqual(str(self.bst), "[ 1 ]")
            self.assertEqual(self.bst.get_height(), 1)

    def test_insertion_of_same_value_at_leaf(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        try:
            self.bst.insert_element(1)
        except ValueError:
            self.assertEqual(str(self.bst), "[ 1, 2 ]")
            self.assertEqual(self.bst.get_height(), 2)

    def test_insertion_of_same_value_at_root(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        try:
            self.bst.insert_element(1)
        except ValueError:
            self.assertEqual(str(self.bst), "[ 1, 2 ]")
            self.assertEqual(self.bst.get_height(), 2)

    def test_removal_on_empty(self):
        try:
            self.bst.remove_element(1)
        except ValueError:
            self.assertEqual(str(self.bst), "[ ]")
            self.assertEqual(self.bst.get_height(), 0)

    def test_remove_nonexistant_on_perfect_tree(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(3)
        try:
            self.bst.remove_element(0)
        except ValueError:
            self.assertEqual(str(self.bst), "[ 1, 2, 3 ]")
            self.assertEqual(self.bst.get_height(), 2)
    
    # One more than a three element perfect tree
    def test_one_more_than_perfect_3_height(self):
        self.bst.insert_element(44)
        self.bst.insert_element(55)
        self.bst.insert_element(22)
        self.bst.insert_element(33)
        self.assertEqual(self.bst.get_height(), 3)

    def test_one_more_than_perfect_3_string(self):
        self.bst.insert_element(44)
        self.bst.insert_element(55)
        self.bst.insert_element(22)
        self.bst.insert_element(33)
        self.assertEqual(str(self.bst), "[ 22, 33, 44, 55 ]")

    def test_one_more_than_perfect_3_in_order(self):
        self.bst.insert_element(44)
        self.bst.insert_element(55)
        self.bst.insert_element(22)
        self.bst.insert_element(33)
        self.assertEqual(self.bst.in_order(), "[ 22, 33, 44, 55 ]")

    def test_one_more_than_perfect_3_pre_order(self):
        self.bst.insert_element(44)
        self.bst.insert_element(55)
        self.bst.insert_element(22)
        self.bst.insert_element(33)
        self.assertEqual(self.bst.pre_order(), "[ 44, 22, 33, 55 ]")

    def test_one_more_than_perfect_3_post_order(self):
        self.bst.insert_element(44)
        self.bst.insert_element(55)
        self.bst.insert_element(22)
        self.bst.insert_element(33)
        self.assertEqual(self.bst.post_order(), "[ 33, 22, 55, 44 ]")

    # three elements rotate left
    def test_rotate_left_height(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.get_height(), 2)

    def test_rotate_left_string(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.bst.insert_element(3)
        self.assertEqual(str(self.bst), "[ 1, 2, 3 ]")

    def test_rotate_left_in_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.in_order(), "[ 1, 2, 3 ]")

    def test_rotate_left_pre_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.pre_order(), "[ 2, 1, 3 ]")

    def test_rotate_left_post_order(self):
        self.bst.insert_element(1)
        self.bst.insert_element(2)
        self.bst.insert_element(3)
        self.assertEqual(self.bst.post_order(), "[ 1, 3, 2 ]")

    # three elements rotate right
    def test_rotate_right_height(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.get_height(), 2)

    def test_rotate_right_string(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.assertEqual(str(self.bst), "[ 1, 2, 3 ]")

    def test_rotate_right_in_order(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.in_order(), "[ 1, 2, 3 ]")

    def test_rotate_right_pre_order(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.pre_order(), "[ 2, 1, 3 ]")

    def test_rotate_right_post_order(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.post_order(), "[ 1, 3, 2 ]")

    def test_rotate_left_with_float_height(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.insert_element(6)
        self.assertEqual(self.bst.get_height(), 3)

    def test_rotate_left_with_float_string(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.insert_element(6)
        self.assertEqual(str(self.bst), "[ 1, 2, 3, 4, 5, 6 ]")

    # With the knowledge that in_order is the same as string, and string simply calls in order, from now on I'll be skipping the in order call.

    def test_rotate_left_with_float_pre_order(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.insert_element(6)
        self.assertEqual(self.bst.pre_order(), "[ 4, 2, 1, 3, 5, 6 ]")

    def test_rotate_left_with_float_post_order(self):
        self.bst.insert_element(2)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.insert_element(6)
        self.assertEqual(self.bst.post_order(), "[ 1, 3, 2, 6, 5, 4 ]")

    def test_rotate_right_with_float_height(self):
        self.bst.insert_element(5)
        self.bst.insert_element(3)
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(4)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.get_height(), 3)

    def test_rotate_right_with_float_string(self):
        self.bst.insert_element(5)
        self.bst.insert_element(3)
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(4)
        self.bst.insert_element(1)
        self.assertEqual(str(self.bst), "[ 1, 2, 3, 4, 5, 6 ]")

    def test_rotate_right_with_float_pre_order(self):
        self.bst.insert_element(5)
        self.bst.insert_element(3)
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(4)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.pre_order(), "[ 3, 2, 1, 5, 4, 6 ]")

    def test_rotate_right_with_float_post_order(self):
        self.bst.insert_element(5)
        self.bst.insert_element(3)
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(4)
        self.bst.insert_element(1)
        self.assertEqual(self.bst.post_order(), "[ 1, 2, 4, 6, 5, 3 ]")

    # left, right imbalance
    def test_rotate_left_then_right_height(self):
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(8)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.remove_element(8)
        self.assertEqual(self.bst.get_height(), 3)

    def test_rotate_left_then_right_string(self):
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(8)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.remove_element(8)
        self.assertEqual(str(self.bst), "[ 1, 2, 3, 4, 5, 6, 7 ]")

    def test_rotate_left_then_right_pre_order(self):
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(8)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.remove_element(8)
        self.assertEqual(self.bst.pre_order(), "[ 4, 2, 1, 3, 6, 5, 7 ]")

    def test_rotate_left_then_right_post_order(self):
        self.bst.insert_element(6)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(4)
        self.bst.insert_element(8)
        self.bst.insert_element(3)
        self.bst.insert_element(5)
        self.bst.remove_element(8)
        self.assertEqual(self.bst.post_order(), "[ 1, 3, 2, 5, 7, 6, 4 ]")

    # right,left imbalance
    def test_rotate_right_then_left_height(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(5)
        self.bst.insert_element(8)
        self.bst.insert_element(4)
        self.bst.insert_element(6)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.get_height(), 3)

    def test_rotate_right_then_left_string(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(5)
        self.bst.insert_element(8)
        self.bst.insert_element(4)
        self.bst.insert_element(6)
        self.bst.remove_element(1)
        self.assertEqual(str(self.bst), "[ 2, 3, 4, 5, 6, 7, 8 ]")

    def test_rotate_right_then_left_pre_order(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(5)
        self.bst.insert_element(8)
        self.bst.insert_element(4)
        self.bst.insert_element(6)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.pre_order(), "[ 5, 3, 2, 4, 7, 6, 8 ]")

    def test_rotate_right_then_left_post_order(self):
        self.bst.insert_element(3)
        self.bst.insert_element(2)
        self.bst.insert_element(7)
        self.bst.insert_element(1)
        self.bst.insert_element(5)
        self.bst.insert_element(8)
        self.bst.insert_element(4)
        self.bst.insert_element(6)
        self.bst.remove_element(1)
        self.assertEqual(self.bst.post_order(), "[ 2, 4, 3, 6, 8, 7, 5 ]")


if __name__ == '__main__':
    unittest.main()
