#!/usr/bin/python3
# 1-square.py
# fuadhasen
"""define square class with size"""


class Square:
    """class with size private attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """get the private value using public.
        special attribute size provided by property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the property.

        Args:
            value (any): The new value to set for the property.
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area function"""
        return self.size * self.size
