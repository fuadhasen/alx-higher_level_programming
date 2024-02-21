#!/usr/bin/python3
"""This module provide function that write file. """


def write_file(filename="", text=""):
    """function that write file."""
    with open(filename, "w") as f:
        nb = f.write(text)
    return nb
