#!/usr/bin/python3
""" mod doc """


def add_attribute(obj, name, value):
    """ func doc """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
