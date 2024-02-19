#!/usr/bin/python3
"""This module povide a function that check obj
   is instance of class inherited from  parent class."""


def inherits_from(obj, a_class):
    """ function check wether given obj is instance class that
        inherited from parent class but not from parent.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
