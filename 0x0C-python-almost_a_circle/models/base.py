#!/usr/bin/python3
""" Base Module """
import json
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save Base instances to a file"""
        with open(cls.__name__ + '.json', 'w') as f:
            things = [x.to_dictionary() for x in list_objs]
            f.write(Base.to_json_string(things))

    @classmethod
    def load_from_file(cls):
        """Load Base instances from a file"""
        with open(cls.__name__ + '.json', 'r') as f:
            return [cls.create(**x) for x in Base.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + '.csv', 'w') as f:
            text = ''
            for o in list_objs:
                if cls.__name__ == 'Square':
                    fs = '{:d},{:d},{:d},{:d}\n'
                    text += fs.format(o.id, o.size, o.x, o.y)
                else:
                    fs = '{:d},{:d},{:d},{:d},{:d}\n'
                    text += fs.format(o.id, o.width, o.height, o.x, o.y)
            f.write(text)

    @classmethod
    def load_from_file_csv(cls):
        objects = []
        with open(cls.__name__ + '.csv', 'r') as f:
            for line in f:
                args = list(map(int, line.split(',')))
                new = cls(1, 1)
                new.update(*args)
                objects.append(new)
        return objects

    @classmethod
    def create(cls, **dictionary):
        """Create a new Base instance with kwargs"""
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        pen = turtle.Turtle()
        pen.speed(3)
        for rect in list_rectangles + list_squares:
            pen.up()
            pen.goto(0, 0)
            pen.forward(rect.x)
            pen.right(90)
            pen.forward(rect.y)
            pen.down()

            pen.begin_fill()
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.end_fill()