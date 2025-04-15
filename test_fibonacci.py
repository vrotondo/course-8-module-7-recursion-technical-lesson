import unittest
from lib.fibonacci import fibonacci, fibonacci_debug

class TestFibonacci(unittest.TestCase):

    def test_base_case_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_base_case_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_small_number(self):
        self.assertEqual(fibonacci(5), 5)  # Sequence: 0, 1, 1, 2, 3, 5

    def test_medium_number(self):
        self.assertEqual(fibonacci(7), 13)  # Sequence: ..., 8, 13

    def test_debug_function_matches_normal(self):
        # Compare against expected known values instead of matching unimplemented functions
        expected = [0, 1, 1, 2, 3, 5, 8]
        for n, result in enumerate(expected):
            self.assertEqual(fibonacci_debug(n), result)


if __name__ == '__main__':
    unittest.main()
