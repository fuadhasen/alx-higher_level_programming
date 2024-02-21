#!/usr/bin/python3
"""This module provide function that Save Object to file. """

import json


def save_to_json_file(my_obj, filename):
    """function that save object to file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
