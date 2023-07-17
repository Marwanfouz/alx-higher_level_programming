#!/usr/bin/python3
"""Define a base module class."""
import json


class Base:
    """the Base class for all classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as js:
            if list_objs is None:
                return "[]"
            else:
                list_dicts = [x.to_dictionary() for x in list_objs]
                js.write(Base.to_json_string(list_dicts))
