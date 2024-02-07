#!/usr/bin/python3
# 1-square.py
# fuadhasen
"""define square class with size"""


class Square:
    """class with size private attribute"""
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
