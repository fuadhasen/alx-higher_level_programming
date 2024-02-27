#!/usr/bin/python3
"""This module provide Base class. """
import json


class Base:
    """Base class. """
    __nb_object = 0

    def __init__(self, id=None):
        """class constructor. """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_object += 1
            self.id = type(self).__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json representation. """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to the file. """
        if list_objs is None:
            list_objs = []
        list_dic = []
        filename = cls.__name__ + ".json"
        for rec in list_objs:
            list_dic.append(cls.to_dictionary(rec))

        _dict = cls.to_json_string(list_dic)
        with open(filename, "w") as f:
            f.write(_dict)
