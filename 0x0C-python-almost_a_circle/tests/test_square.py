#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import unittest
"""
    unittest — Unit testing framework
    tests for class Square
"""
import pep8
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/square.py", show_source=True)
        file_error = check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ Method called immediately before calling the test method """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Method called immediately after calling the test method """
        pass
