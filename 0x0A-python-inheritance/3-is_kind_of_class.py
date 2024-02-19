#!/usr/bin/python3
"""This module povide a function that check instance
   of object and subclass."""


def is_kind_of_class(obj, a_class):
    """ function check wether given obj is instance of
      given class and subclass.
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
