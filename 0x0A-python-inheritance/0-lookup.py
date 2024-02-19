#!/usr/bin/python3
"""This Module Provide A function that return list of available attribut.
"""


def lookup(obj):
    """This function return available attribut
       and method of an object.
    """

    return dir(obj)
