#!/usr/bin/python3
"""This module provide function that Create object from a JSON file. """
import json


def load_from_json_file(filename):
    """function that creat obj from .json file."""
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
