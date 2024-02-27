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
        # befor iencoding convert
        # none serializable to serializablw object
        serialize_list = []
        for i in list_dictionaries:
            serialize_dict = {}
            for k, v in i.items():
                if not isinstance(v, (int, float, str, None, bool, list, dict)):
                    serialize_dict[k] = str(v)
                else:
                    serialize_dict[k] = v
            serialize_list.append(serialize_dict)
        return json.dumps(serialize_list)
