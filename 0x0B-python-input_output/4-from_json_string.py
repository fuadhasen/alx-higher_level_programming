#!/usr/bin/python3
"""This module provide function that return object
   represented by JSON string. """

import json


def from_json_string(my_str):
    """function return obj from json represntation."""
    js_obj = json.loads(my_str)
    return js_obj
