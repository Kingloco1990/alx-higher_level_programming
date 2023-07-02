#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 2, 3, 5, 4, 4, 5]), 5)


if __name__ == '__main__':
    unittest.main()
