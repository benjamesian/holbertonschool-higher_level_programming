#!/usr/bin/python3
""" Base Module """
import json


class Base:
    """Base Geometry"""
    __nb_objects = 0


    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + '.json', 'w') as f:
            things = [x.to_dictionary() for x in list_objs]
            f.write(Base.to_json_string(things))
