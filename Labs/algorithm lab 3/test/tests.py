import unittest
import sys
import os
sys.path.append(os.path.abspath('..')) 
from src.bruteforce import bruteforce
from src.dynamic import dynamic_knapsack
from src.greedy import greedy_knapsack
from src.bruteforcefractional import fractional_knapsack

class TestKnapsack(unittest.TestCase):

    def test_bruteforce(self):
        profit = [20, 20, 40, 60]
        weights = [5, 4, 2, 3]
        capacity = 10
        self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (120,['0', '1', '1', '1']))

    def test_dynamic(self):
        profit = [50, 100, 150, 200]
        weights = [8, 16, 32, 40]
        capacity = 64
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), 350)


    def test_fractional_knapsack(self):
        # Test case 1
        item_weights = [10, 20, 30]
        item_profits = [60, 100, 120]
        max_capacity = 50
        expected_max_profit = 240.0

        self.assertEqual(fractional_knapsack(item_weights, item_profits, max_capacity),(expected_max_profit,[1, 1, 0.6666666666666666]))


        # Test case 2
        item_profits = [50, 100, 150, 200]
        item_weights = [8, 16, 32, 40]
        max_capacity = 64
        expected_max_profit = 350

        self.assertEqual(fractional_knapsack(item_weights, item_profits, max_capacity),(expected_max_profit,[1, 1, 0, 1]))

    def test_greedy_knapsack(self):
        profit = [50, 100, 150, 200]
        weights = [8, 16, 32, 40]
        capacity = 64
        factor = [p / w for p, w in zip(profit, weights)]
        self.assertEqual(greedy_knapsack(profit, weights, capacity, factor), (350, ['1', '1', '0', '1']))

    def test_empty_knapsack(self):
        profit = []
        weights = []
        capacity = 10
        self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (0, []))
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), 0)
        self.assertEqual(greedy_knapsack(profit, weights, capacity, []), (0, []))
        self.assertEqual(fractional_knapsack(weights,profit, capacity), (0, []))

    def test_single_item_fits(self):
        profit = [20]
        weights = [5]
        capacity = 5
        #self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (20,[]))
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), 20)
        self.assertEqual(greedy_knapsack(profit, weights, capacity, [20/5]), (20,["1"]))
        self.assertEqual(fractional_knapsack(weights,profit,capacity), 20,[1])

    def test_single_item_does_not_fit(self):
        profit = [20]
        weights = [5]
        capacity = 3
        self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (0, []))
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), 0)
        self.assertEqual(greedy_knapsack(profit, weights, capacity, [20/5]), (12, [0.6]))

    def test_multiple_items_same_ratio(self):
        profit = [20, 30, 40, 50]
        weights = [5, 10, 15, 20]
        capacity = 30
        factor = [p / w for p, w in zip(profit, weights)]
        self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (90,['1', '1', '1', '0']))
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), 90)
        self.assertEqual(greedy_knapsack(profit, weights, capacity, factor), (90,['1', '1', '1', '0']))

    def test_max_capacity(self):
        profit = [20, 30, 40, 50]
        sum_of_profit=sum(profit)
        weights = [5, 10, 15, 20]
        capacity = sum(weights)
        self.assertEqual(bruteforce(capacity, len(profit), profit, weights), (sum_of_profit,['1', '1', '1', '1']))
        self.assertEqual(dynamic_knapsack(len(profit), capacity, profit, weights), sum_of_profit)
        self.assertEqual(greedy_knapsack(profit, weights, capacity, [p / w for p, w in zip(profit, weights)]), (sum_of_profit,['1', '1', '1', '1']))

if __name__ == '__main__':
    unittest.main()
