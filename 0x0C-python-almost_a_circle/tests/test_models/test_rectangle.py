#!/usr/bin/python3
""" Tests for Rectangle class """
import unittest
from models import rectangle
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Called before each test is run"""
        self.r = Rectangle(1, 1, 1, 1, 1)

    def test_init(self):
        """Test the `init` method"""
        r = Rectangle(1, 1)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 1, 0, 0))
        self.assertIsInstance(r.id, int)

    def test_id(self):
        """Test id setting on Base class"""
        self.assertEqual(self.r.id, 1)

    def test_str(self):
        """Test for __str__ method"""
        s = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(str(self.r), s)

    def test_width_type(self):
        """Test for setting width attr"""
        with self.assertRaises(TypeError):
            Rectangle(1.0, 1)

    def test_height_type(self):
        """Test for setting height attr"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1.0)

    def test_x_type(self):
        """Test for x attr"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, x=1.0)

    def test_y_type(self):
        """Test for y attr"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, y=1.0)

    def test_width_value(self):
        """Test for width attr"""
        self.assertEqual(self.r.width, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_height_value(self):
        """Test for height attr"""
        self.assertEqual(self.r.height, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_x_value(self):
        """Test for x attr"""
        self.assertEqual(self.r.x, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, x=-1)

    def test_y_value(self):
        """Test for y attr"""
        self.assertEqual(self.r.y, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, y=-1)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.r.area(), 1)
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)

    def test_display(self):
        """Test the display method"""
        r = Rectangle(1, 1)
        self.out = StringIO()
        sys.stdout = self.out
        r.display()
        self.assertEqual(self.out.getvalue(), '#\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Rectangle(2, 2)
        r.display()
        self.assertEqual(self.out.getvalue(), '##\n##\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Rectangle(1, 1, 1, 1)
        r.display()
        self.assertEqual(self.out.getvalue(), '\n #\n')
        sys.stdout = sys.__stdout__

    def test_update_args(self):
        """Test update method with *args provided"""
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (1, 1, 1, 1, 1))
        r.update(2, 3, 4, 5, 6)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 3, 4, 5, 6))

    def test_update_kwargs(self):
        """Test update method with **kwargs provided"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**{'id': 2, 'x': 3, 'y': 4, 'width': 5, 'height': 6})
        self.assertEqual((r.id, r.x, r.y, r.width, r.height), (2, 3, 4, 5, 6))

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        d = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        self.assertEqual(self.r.to_dictionary(), d)
        self.r.my_fun_new_attr = 42
        self.assertEqual(self.r.to_dictionary(), d)


if __name__ == '__main__':
    unittest.main()
