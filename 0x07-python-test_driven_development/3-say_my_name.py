#!/usr/bin/python3
# fuad hassen
# 3-say_my_name.py
""" This module provide a function that print string """


def say_my_name(first_name, last_name=""):
    """print string.

    Args:
        first_name (str): first arg.
        last_name (str): last arg.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
