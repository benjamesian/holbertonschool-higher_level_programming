#!/usr/bin/python3
""" An Empty Rectangle """


class Rectangle:
    """ A Rectangle with a representation """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return (self.height * ('#' * self.width + '\n')).strip()

    def __repr__(self):
        """ Representation of instance constructor """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    @property
    def width(self):
        """ Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width to the value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
