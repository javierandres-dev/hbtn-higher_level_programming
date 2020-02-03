#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
import unittest
"""
    unittest — Unit testing framework
    tests for class Base
"""
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

    def test_id_0main(self):
        """ test 0-main cases """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(89)
        self.assertEqual(b4.id, 89)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_empty(self):
        """ test empty case """
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)

    def test_id_int(self):
        """ test integer case """
        self.b1 = Base(1)
        self.assertEqual(self.b1.id, 1)

    def test_id_zero(self):
        """ test zero case """
        self.b1 = Base(0)
        self.assertEqual(self.b1.id, 0)

    def test_id_neg(self):
        """ test negative case """
        self.b1 = Base(-1)
        self.assertEqual(self.b1.id, -1)

    def test_id_float(self):
        """ test the float case """
        self.b1 = Base(1.2)
        self.assertEqual(self.b1.id, 1.2)

    def test_id_str(self):
        """ test string case """
        self.b1 = Base("testing")
        self.assertEqual(self.b1.id, "testing")

    def test_id_list(self):
        """ test list case """
        self.b1 = Base([1, 2, 3])
        self.assertEqual(self.b1.id, [1, 2, 3])

    def test_id_tup(self):
        """ test tuple case """
        self.b1 = Base((1, 2, 3))
        self.assertEqual(self.b1.id, (1, 2, 3))

    def test_id_dict(self):
        """ test dictionary case """
        self.b1 = Base({'a': 1, 'b': 2})
        self.assertEqual(self.b1.id, {'a': 1, 'b': 2})

    def test_serialization(self):
        """ convert from python to jason """
        p0 = None
        j0 = Base.to_json_string(p0)
        self.assertEqual(j0, "[]")
        self.assertEqual(type(j0), str)

        p1 = []
        j1 = Base.to_json_string(p1)
        self.assertEqual(j1, "[]")
        self.assertEqual(type(j1), str)

        p2 = [{}]
        j2 = Base.to_json_string(p2)
        self.assertEqual(j2, "[{}]")
        self.assertEqual(type(j2), str)

        p3 = [{'x': 1, 'y': 2}]
        j3 = Base.to_json_string(p3)
        st = str(p3)
        self.assertEqual(j3, st.replace("'", "\""))
        self.assertEqual(type(j3), str)

        p4 = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        j4 = Base.to_json_string(p4)
        st = str(p4)
        self.assertEqual(j4, st.replace("'", "\""))
        self.assertEqual(type(j4), str)
