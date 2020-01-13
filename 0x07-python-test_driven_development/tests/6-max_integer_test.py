#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ methods for testing the function 'max_integer()' """
    def test_greater(self):
        """ find greater  """
        self.assertAlmostEqual(max_integer([-2, -1, 0, 1, 2, 3, 4]), 4)

    def test_empty(self):
        """ find empty  """
        self.assertAlmostEqual(max_integer(), None)

    def test_null(self):
        """ find null  """
        self.assertAlmostEqual(max_integer([None]), None)
