#!/usr/bin/python3
"""This module provide function that write file. """


def write_file(filename="", text=""):
    """function that read file."""
    with open(filename, "w") as f:
        f.write(text)
