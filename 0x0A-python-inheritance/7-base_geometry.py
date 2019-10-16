#!/usr/bin/python3
""" Base Class """


class BaseGeometry:
    """ Base Class """
    def area(self):
        """ get area of a shape """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate that value if a positive integer """
        if type(value) != int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
