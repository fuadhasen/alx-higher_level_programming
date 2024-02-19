#!/usr/bin/python3
"""This module povide a function that check instance
   of object."""


def is_same_class(obj, a_class):
    """ function check wether given obj is instance of
      given class.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True

    
