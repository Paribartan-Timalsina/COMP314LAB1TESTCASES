# tests/test_sorting.py
import sys
import os
sys.path.append(os.path.abspath('..')) 
import math
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort
from src.merge import merge
from src.partition import partition
import unittest
import random

# Defines a test class `UnitTest` that inherits from `unittest.TestCase`.
class UnitTest(unittest.TestCase):

    # Test method for verifying the correct functionality of the merge sort algorithm.
    def test_sortmerge(self):
        input_data = [2, 3, 1, 0, 5]
        # Calls the `merge_sort` function with the sample list and stores the result.
        result = merge_sort(input_data,0,len(input_data)-1)
        # Asserts that the result of the merge sort matches the expected sorted list.
        self.assertListEqual(result, [0, 1, 2, 3, 5])

      # Test method for verifying the correct functionality of the quick sort algorithm.
    def test_sortquick(self):
        # Similar to the merge sort test, defines a sample input list for quick sort.
        input_data = [2, 3, 1, 0, 5]
        # Calls the `quick_sort` function with the sample list and stores the result.
        result = quick_sort(input_data,0,len(input_data)-1)
        # Asserts that the result of the selection sort matches the expected sorted list.
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    # Test method for ensuring both sorting algorithms can handle an empty list.
    def test_sortzero(self):
        # Defines an empty list.
        input_data = []
        # Sorts the empty list using both algorithms.
        result3=merge_sort(input_data,0,len(input_data)-1)
        result4=quick_sort(input_data,0,len(input_data)-1)
        # Asserts that sorting an empty list returns an empty list for both algorithms.
        self.assertListEqual(result3, [])
        self.assertListEqual(result4, [])

    def test_merge(self):
        #Test merge algorithm with input data
        input_data1 = [1, 2, 3, 0, 5]
        middle = math.floor((0+len(input_data1)-1) / 2)
        #calls the merge function
        result= merge(input_data1,0,middle,len(input_data1)-1)
        # Asserts that the result of the selection sort matches the expected sorted list.
        self.assertListEqual(result, [0, 1, 2, 3, 5])

        
        # Test with another input data
        input_data2 = [ 1,5,9, 2, 4, 7]
        middle = math.floor((0 + len(input_data2) - 1) / 2)
        #calls the merge function 
        result = merge(input_data2, 0, middle, len(input_data2) - 1)
        # Asserts that the result of the selection sort matches the expected sorted list.
        self.assertListEqual(result, [1, 2, 4, 5, 7, 9])

    def test_partition(self):
        # Test with a input data
        input_data = [2, 1, 5, 0, 3]
        index=partition(input_data,0,len(input_data)-1)
        #Verifies the correct index in returned
        self.assertEqual(index,3)

         # Test with random input data
        random_data = random.sample(range(100), 10)  # Generating random data
        index = partition(random_data, 0, len(random_data) - 1)
        # Verifying that elements before the pivot are less than or equal to it
        for i in range(index):
            self.assertLessEqual(random_data[i], random_data[index])
        # Verifying that elements after the pivot are greater than the pivot
        for i in range(index + 1, len(random_data)):
            self.assertGreater(random_data[i], random_data[index])

    # Test method for ensuring both sorting algorithms work correctly with a single-element list.
    def test_sortone(self):
        # Defines a list with a single element.
        input_data = [1]
        # Sorts the single-element list using both algorithms.
        result3=merge_sort(input_data,0,len(input_data)-1)
        result4=quick_sort(input_data,0,len(input_data)-1)
        # Asserts that sorting a single-element list returns the same list for both algorithms.
        self.assertListEqual(result3, [1])
        self.assertListEqual(result4, [1])

    # Test method for ensuring both sorting algorithms correctly identify and do not alter an already sorted list.
    def test_sort_sorted(self):
        # Defines an already sorted list.
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Sorts the already sorted list using both algorithms.
        result3=merge_sort(input_data,0,len(input_data)-1)
        result4=quick_sort(input_data,0,len(input_data)-1)
        # Asserts that both algorithms do not alter an already sorted list.
        self.assertListEqual(result3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(result4, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# Checks if the script is the main program and runs the tests if it is.
if __name__ == "__main__":
    unittest.main()
