#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for class Base
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/base.py", show_source=True)
        file_error= check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ Method called immediately before calling the test method """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Method called immediately after calling the test method """
        pass

    def test_id(self):
        """ test predefined cases """
        pass

    def test_0(self):
        """ test zero case """
        self.b1 = Base(0)
        self.assertEqual(self.b1.id, 0)

    def test_neg(self):
        """ test negative case """
        self.b1 = Base(-1)
        self.assertEqual(self.b1.id, -1)

    def test_float(self):
        """ test the float case """
        self.b1 = Base(1.2)
        self.assertEqual(self.b1.id, 1.2)

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
