#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_single_element(self):
        """Test single element list"""
        self.assertEqual(max_integer([98]), 98)

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test mixed positive and negative"""
        self.assertEqual(max_integer([-10, 5, 3, 99, -20]), 99)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_float_numbers(self):
        """Test float numbers"""
        self.assertEqual(max_integer([1.5, 2.8, 0.9]), 2.8)

    def test_string(self):
        """Test string"""
        self.assertEqual(max_integer("Brenna"), "r")


if __name__ == "__main__":
    unittest.main()
