#!/usr/bin/python3
"""This module provide function that read file. """


def read_file(filename=""):
    """function that read file."""
    with open(filename, "r", encoding="UTF8") as f:
        text = f.read()
    print(text, end="")
