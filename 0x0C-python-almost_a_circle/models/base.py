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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to the file. """
        list_dic = []
        filename = list_objs[0].__class__.__name__ + ".json"
        for rec in list_objs:
            list_dic.append(cls.to_dictionary(rec))

        _dict = cls.to_json_string(list_dic)
        with open(filename, "w") as f:
            if _dict is []:
                f.write([])
            else:
                f.write(_dict)
