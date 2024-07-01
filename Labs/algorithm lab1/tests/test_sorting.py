# tests/test_sorting.py
import sys
import os
sys.path.append(os.path.abspath('..')) 
import math
from src.insertion_sort import insertion_sort
from src.selection_sort import selection_sort
import unittest
import random

# Defines a test class `UnitTest` that inherits from `unittest.TestCase`.
class UnitTest(unittest.TestCase):
    # Test method for verifying the correct functionality of the insertion sort algorithm.
    def test_sortinsertion(self):
        # Defines a sample input list to be sorted.
        input_data = [2, 3, 1, 0, 5]
        # Calls the `insertion_sort` function with the sample list and stores the result.
        result = insertion_sort(input_data)
        # Asserts that the result of the insertion sort matches the expected sorted list.
        self.assertListEqual(result, [0, 1, 2, 3, 5])
    
    # Test method for verifying the correct functionality of the selection sort algorithm.
    def test_sortselection(self):
        # Similar to the insertion sort test, defines a sample input list for selection sort.
        input_data = [2, 3, 1, 0, 5]
        # Calls the `selection_sort` function with the sample list and stores the result.
        result = selection_sort(input_data)
        # Asserts that the result of the selection sort matches the expected sorted list.
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    # Test method for ensuring both sorting algorithms can handle an empty list.
    def test_sortzero(self):
        # Defines an empty list.
        input_data = []
        # Sorts the empty list using both algorithms.
        result1 = insertion_sort(input_data)
        result2 = selection_sort(input_data)

        # Asserts that sorting an empty list returns an empty list for both algorithms.
        self.assertListEqual(result1, [])
        self.assertListEqual(result2, [])
    

    # Test method for ensuring both sorting algorithms work correctly with a single-element list.
    def test_sortone(self):
        # Defines a list with a single element.
        input_data = [1]
        # Sorts the single-element list using both algorithms.
        result1 = insertion_sort(input_data)
        result2 = selection_sort(input_data)
        # Asserts that sorting a single-element list returns the same list for both algorithms.
        self.assertListEqual(result1, [1])
        self.assertListEqual(result2, [1])

    # Test method for ensuring both sorting algorithms correctly identify and do not alter an already sorted list.
    def test_sort_sorted(self):
        # Defines an already sorted list.
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Sorts the already sorted list using both algorithms.
        result1 = insertion_sort(input_data)
        result2 = selection_sort(input_data)
        # Asserts that both algorithms do not alter an already sorted list.
        self.assertListEqual(result1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(result2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        
if __name__ == "__main__":
    unittest.main()
