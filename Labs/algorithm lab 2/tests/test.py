# tests/test_first.py
import sys
import os
sys.path.append(os.path.abspath('..')) 


# Import the unittest module for creating and running tests.
import unittest
# Import the sum function from the first module located within the src directory.
from src.first import sum

# Define a class named UnitTest, which inherits from unittest.TestCase.
# This class will contain the test cases for the sum function.
class UnitTest(unittest.TestCase):
    # Define a test case method to test the sum function with a list of numbers.
    def test_sum(self):
        # Prepare input data: a list of numbers whose sum is known.
        input_data = [9, 1, 2]
        # Call the sum function with the input data and store the result.
        result = sum(input_data)
        # Assert that the result returned by the sum function is equal to 12,
        # which is the expected sum of the numbers in the input list.
        self.assertEqual(result, 12)
    
    # Define another test case method to test the sum function with an empty list.
    def test_sum_empty(self):
        # Prepare input data: an empty list.
        input_data = []
        # Call the sum function with the empty list and store the result.
        result = sum(input_data)
        # Assert that the result returned by the sum function is 0,
        # which is the expected sum of an empty list.
        self.assertEqual(result, 0)
    
# This block checks if the script is being run directly and not being imported into another script.
if __name__ == "__main__":
    unittest.main()
