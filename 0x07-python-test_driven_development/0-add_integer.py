#!/usr/bin/python3
"""
A function for adding two integers
"""


def add_integer(a, b=98):
    """ Addition function """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
