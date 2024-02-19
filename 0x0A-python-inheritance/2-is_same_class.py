#!/usr/bin/python3
"""This module povide a function that check instance
   of object."""


def is_same_class(obj, a_class):
    """ function check wether given obj is instance of
      given class.
    """
    if type(obj) is a_class:
        return True
    return False

    
