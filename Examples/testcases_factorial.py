import unittest
from factorial_of_number import factorial

class FactorialTestCase(unittest.TestCase):
    def test_factorial_positive_number(self):
        # Test case for a positive number
        result = factorial(5)  # initial name of a function
        self.assertEqual(result, 120)

    def test_factorial_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)  # Test case for zero

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)