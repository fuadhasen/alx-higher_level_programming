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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        expected_key = ['id', 'width', 'height', 'x', 'y']
        for dic in list_dictionaries:
            if not set(dic.keys()).issubset(expected_key):
                raise ValueError("there is inconsistency of key")
        return json.dumps(list_dictionaries)
