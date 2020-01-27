#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for class Square
"""
import unittest
import pep8
from models.square import Square

class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/square.py", show_source=True)
        file_error = check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ method raises an exception while the test is running """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ method that tidies up after the test method has been run """
        pass
