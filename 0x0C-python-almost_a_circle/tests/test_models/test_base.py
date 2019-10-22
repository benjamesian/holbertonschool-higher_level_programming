#!/usr/bin/python3
""" Tests for Base geometry class """
import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """Class for testing the Base geometry class"""
    def __init__(self, testname):
        super(TestBase, self).__init__(testname)
        self.d = Base()

    def test_id(self):
        """Test id setting on Base class"""
        self.assertEqual(self.d.id, 1)
        nxt = Base(12)
        self.assertEqual(nxt.id, 12)

    def test_same_id(self):
        """Objects with same id are not the same"""
        a = Base(1)
        b = Base(1)
        self.assertEqual(a.id, b.id)
        self.assertIsNot(a, b)


if __name__ == '__main__':
    unittest.main()
