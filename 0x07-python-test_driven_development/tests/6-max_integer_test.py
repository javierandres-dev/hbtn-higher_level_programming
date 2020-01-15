#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ methods for testing the function 'max_integer()' """
    def test_null(self):
        """ find greater- list null  """
        self.assertAlmostEqual(max_integer([None]), None)

    def test_empty(self):
        """ find greater - list is empty  """
        self.assertAlmostEqual(max_integer(), None)

    def test_greater(self):
        """ find greater - list of one element """
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_greater(self):
        """ find greater - max at the beginning """
        self.assertAlmostEqual(max_integer([2, 1]), 2)

    def test_greater(self):
        """ find greater - max in the middle """
        self.assertAlmostEqual(max_integer([1, 3, 2]), 3)

    def test_greater(self):
        """ find greater - max at the end """
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0, 1, 2, 3, 4]), 4)

    def test_greater(self):
        """ find greater - one negative number in the list """
        self.assertAlmostEqual(max_integer([-1, 0, 1, 2, 3, 4, 5]), 5)

    def test_greater(self):
        """ find greater - only negative numbers in the list """
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1]), -1)
