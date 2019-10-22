#!/usr/bin/python3
""" Tests for Base geometry class """
import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """Class for testing the Base geometry class"""

    def test_id(self):
        """Test id setting on Base class"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_same_id(self):
        """Objects with same id are not the same"""
        a = Base(1)
        b = Base(1)
        self.assertEqual(a.id, b.id)
        self.assertIsNot(a, b)

    def test_to_json_string(self):
        """test converstion of python object to a json string"""
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'a': 1}]), '[{"a": 1}]')

    def test_from_json_string(self):
        """test conversion of json string to python object"""
        obj = [{'a': 1}]
        json_string = Base.to_json_string(obj)
        self.assertEqual(Base.from_json_string(json_string), obj)

if __name__ == '__main__':
    unittest.main()
