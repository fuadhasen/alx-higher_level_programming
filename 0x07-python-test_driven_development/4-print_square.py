#!/usr/bin/python3
# Fuad Hassen <fuadhas6634@gmail.com>
# 4-print_square.py
"""This module provide a function that print square. """


def print_square(size):
    """This function print square based on size.

    Args:
        size (int): size of square

    Raise:
        TypeError if the size is not int.
        ValueError if the value is negative.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
