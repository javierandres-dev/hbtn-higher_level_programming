#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for Base class
"""
import unittest
import pep8
from models.base import Base

class verify_pep8(unittest.TestCase):
    """ class """
    def test_pep8(self):
        """ method """
        check = pep8.Checker("models/base.py", show_source=True)
        file_error= check.check_all()
