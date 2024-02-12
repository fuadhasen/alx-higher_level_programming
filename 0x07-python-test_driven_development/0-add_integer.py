#!/usr/bin/python3
# 0-add_integer.py
# fuad hassen
"""define a function that add two int."""


def add_integer(a, b=98):
    """add two integers.

    Args:
        a (int): first argument.
        b (int): second argument.

    Returns:
        (int): sum of a and b.
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be integer")
    if not isinstance(b, int):
        raise TypeError("b must be integer")
    return a + b
