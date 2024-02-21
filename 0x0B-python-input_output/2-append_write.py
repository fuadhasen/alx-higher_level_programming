#!/usr/bin/python3
"""This module provide function that append file. """


def append_write(filename="", text=""):
    """function that append file."""
    with open(filename, "a") as f:
        nb = f.write(text)
    return nb
