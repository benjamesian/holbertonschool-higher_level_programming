#!/usr/bin/python3
""" type checking """


def inherits_from(obj, a_class):
    """ check if subclass """
    return type(obj) != a_class and issubclass(type(obj), a_class)
