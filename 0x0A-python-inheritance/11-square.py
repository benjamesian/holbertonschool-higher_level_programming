#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" My Square """


class Square(Rectangle):
    """ A Square """
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ String Repr of a Square """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
