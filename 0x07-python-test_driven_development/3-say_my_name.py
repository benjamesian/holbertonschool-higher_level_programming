#!/usr/bin/python3
"""
Print a name
"""


def say_my_name(first_name, last_name=""):
    """ Print a name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
