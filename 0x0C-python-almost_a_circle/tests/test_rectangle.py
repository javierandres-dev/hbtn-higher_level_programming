#!/usr/bin/python3
"""
    PEP8 and Unittest for Rectangle class
"""
import pep8
import unittest
from models.base import Base

class format_pep8(unittest.TestCase):
    """ class """
    def test_pep8(self):
        """ method """
        checker = pep8.Checker("models/rectangle.py", show_source=True)
        file_error= checker.check_all()
