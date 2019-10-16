#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ String representation of a Rectangle """
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)

    def area(self):
        """ Area of the Rectangle """
        return self.__width * self.__height
