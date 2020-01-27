#!/usr/bin/python3
"""
    unittest — Unit testing framework
    tests for class Rectangle
"""
import unittest
import pep8
from models.rectangle import Rectangle

class verify_pep8(unittest.TestCase):
    """ class - PEP 8 validated """
    def test_pep8(self):
        """ method - PEP 8 test """
        check = pep8.Checker("models/rectangle.py", show_source=True)
        file_error= check.check_all()

class verify_work(unittest.TestCase):
    """ funcionality test """

    def setUp(self):
        """ method raises an exception while the test is running """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """ method that tidies up after the test method has been run """
        pass

    def test_id(self):
        """ test id cases """
        self.assertEqual(self.r1.id, 35)
        self.assertEqual(self.r2.id, 36)
        self.assertEqual(self.r3.id, 12)

    def test_width(self):
        """ test width cases """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_height(self):
        """ test height cases """
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_x(self):
        """ test x cases """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)


    def test_y(self):
        """ test y cases """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

if __name__ == "__main__":
    unittest.main()
