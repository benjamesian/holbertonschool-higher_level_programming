#!/usr/bin/python3
""" Tests for Square class """
import unittest
from models import square
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    def setUp(self):
        """Called before each test is run"""
        self.r = Square(1, 1, 1, 1)

    def test_init(self):
        """Test the `init` method"""
        r = Square(1)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 1, 0, 0))
        self.assertIsInstance(r.id, int)

    def test_id(self):
        """Test id setting on Base class"""
        self.assertEqual(self.r.id, 1)

    def test_str(self):
        """Test for __str__ method"""
        s = '[Square] (1) 1/1 - 1'
        self.assertEqual(str(self.r), s)

    def test_size_type(self):
        """Test for setting width attr"""
        with self.assertRaises(TypeError):
            Square(1.0)

    def test_x_type(self):
        """Test for x attr"""
        with self.assertRaises(TypeError):
            Square(1, x=1.0)

    def test_y_type(self):
        """Test for y attr"""
        with self.assertRaises(TypeError):
            Square(1, y=1.0)

    def test_size_value(self):
        """Test for size attr"""
        self.assertEqual(self.r.size, 1)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_value(self):
        """Test for x attr"""
        self.assertEqual(self.r.x, 1)
        with self.assertRaises(ValueError):
            Square(1, x=-1)

    def test_y_value(self):
        """Test for y attr"""
        self.assertEqual(self.r.y, 1)
        with self.assertRaises(ValueError):
            Square(1, y=-1)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.r.area(), 1)
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_display(self):
        """Test the display method"""
        r = Square(1)
        self.out = StringIO()
        sys.stdout = self.out
        r.display()
        self.assertEqual(self.out.getvalue(), '#\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Square(2)
        r.display()
        self.assertEqual(self.out.getvalue(), '##\n##\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Square(1, 1, 1)
        r.display()
        self.assertEqual(self.out.getvalue(), '\n #\n')
        sys.stdout = sys.__stdout__

    def test_update_args(self):
        """Test update method with *args provided"""
        r = Square(1, 1, 1, 1)
        self.assertEqual((r.id, r.size, r.x, r.y), (1, 1, 1, 1))
        r.update(2, 3, 4, 5)
        self.assertEqual((r.id, r.size, r.x, r.y), (2, 3, 4, 5))
        r.update()
        self.assertEqual((r.id, r.size, r.x, r.y), (2, 3, 4, 5))

    def test_update_kwargs(self):
        """Test update method with **kwargs provided"""
        r = Square(1, 1, 1, 1)
        r.update(**{'id': 2, 'x': 3, 'y': 4, 'size': 5})
        self.assertEqual((r.id, r.x, r.y, r.size), (2, 3, 4, 5))

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(self.r.to_dictionary(), d)
        self.r.my_fun_new_attr = 42
        self.assertEqual(self.r.to_dictionary(), d)


if __name__ == '__main__':
    unittest.main()
