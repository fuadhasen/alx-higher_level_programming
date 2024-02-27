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
        try:
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            return json.dumps(list_dictionaries)
        except TypeError:
            return "not serializable"
