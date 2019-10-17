#!/usr/bin/python3
""" mod doc """


def add_attribute(obj, name, value):
    """ func doc """
    if not hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
