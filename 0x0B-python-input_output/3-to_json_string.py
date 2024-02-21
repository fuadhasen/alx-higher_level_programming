#!/usr/bin/python3
import json
"""This module provide function that return JSON
   representaion. """


def to_json_string(my_obj):
    """function return json represntation."""
    js_str = json.dumps(my_obj)
    return js_str
