#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for class Base
"""
import unittest
import pep8
from models.base import Base

class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/base.py", show_source=True)
        file_error= check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ method raises an exception while the test is running """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        """ method that tidies up after the test method has been run """
        pass

    def test_id(self):
        """ test predefined cases """
        self.assertEqual(self.b1.id, 13)
        self.assertEqual(self.b2.id, 14)
        self.assertEqual(self.b3.id, 15)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 16)

    def test_0(self):
        """ test zero case """
        self.b1 = Base(0)
        self.assertEqual(self.b1.id, 0)

    def test_neg(self):
        """ test negative case """
        self.b1 = Base(-2)
        self.assertEqual(self.b1.id, -2)

    def test_float(self):
        """ test the float case """
        self.b1 = Base(2.5)
        self.assertEqual(self.b1.id, 2.5)

    def test_str(self):
        """ test string case """
        self.b1 = Base("testing")
        self.assertEqual(self.b1.id, "testing")

    def test_list(self):
        """ test list case """
        self.b1 = Base([1, 2, 3])
        self.assertEqual(self.b1.id, [1, 2, 3])

    def test_tup(self):
        """ test tuple case """
        self.b1 = Base((1, 2, 3))
        self.assertEqual(self.b1.id, (1, 2, 3))

    def test_dict(self):
        """ test dictionary case """
        self.b1 = Base({'a': 1, 'b': 2})
        self.assertEqual(self.b1.id, {'a': 1, 'b': 2})

if __name__ == "__main__":
    unittest.main()
