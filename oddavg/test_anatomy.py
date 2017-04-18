import unittest
from odd_avg import *

class TestOddAvg(unittest.TestCase):
    def test_odd_average(self):
        numbers = [1, 2, 3, 4, 5, 10, 1]
        self.assertEqual(odd_average(numbers), 2.5)

if __name__ == '__main__':
    unittest.main()
