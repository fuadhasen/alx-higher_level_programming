#!/usr/bin/python3
"""This module provide function that return JSON
   representaion. """

import json

def to_json_string(my_obj):
    """function return json represntation."""
    js_str = json.dumps(my_obj)
    return js_str
