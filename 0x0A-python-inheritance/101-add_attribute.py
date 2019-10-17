#!/usr/bin/python3
""" mod doc """


def add_attribute(obj, name, value):
    """ func doc """
    if hasattr(obj, name):
        setattr(obj, name, value)
