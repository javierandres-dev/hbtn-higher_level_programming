#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for Square class
"""
import unittest
import pep8
from models.square import Square

class verify_pep8(unittest.TestCase):
    """ class """
    def test_pep8(self):
        """ method """
        check = pep8.Checker("models/square.py", show_source=True)
        file_error = check.check_all()
