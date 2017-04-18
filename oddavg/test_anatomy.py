import unittest
from odd_avg import *

class TestOddAvg(unittest.TestCase):
    def test_odd_average_with_random_numbers(self):
        numbers = [1, 2, 3, 4, 5, 10, 1]
        self.assertEqual(odd_average(numbers), 2.5)

    def test_odd_average_with_even_numbers(self):
        numbers = [2, 4, 6, 10]
        self.assertEqual(odd_average(numbers), 0)

    def test_odd_average_with_letters(self):
        letters = ["a", "b", "c"]
        self.assertEqual(odd_average(letters), 0)

if __name__ == '__main__':
    unittest.main()
