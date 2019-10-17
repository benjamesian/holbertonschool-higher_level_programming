#!/usr/bin/python3
""" mod doc """


class Student:
    """ Representation of a Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ JSONified Student """
        if attrs and isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            d = {}
            for attr in attrs:
                if attr in self.__dict__:
                    d[attr] = self.dict[attr]
            return d
        return self.__dict__
