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

    def to_json_string(list_dictionaries):
        """ to json representation. """
        for dic in list_dictionaries:
            if dic is None or dic == {}:
                return "[]"
            return json.dumps(dic)
