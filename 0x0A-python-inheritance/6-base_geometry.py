#!/usr/bin/python3
""" Base Class """


class BaseGeometry:
    """ shapes have an area """
    def area(self):
        raise Exception('area() is not implemented')
