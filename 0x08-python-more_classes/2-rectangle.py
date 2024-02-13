#!/usr/bin/python3
# fuad hassen
# 1-rectangle.py
""" This module define class Rectangle """


class Rectangle:
    """ Rectangle class. """

    def __init__(self, width=0, height=0):
        """ intialize constructor.

        Args:
            width (int): frist argument
            height (int): second argument
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width. """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width. """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height. """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        res = self.__width + self.__height
        return 2 * res
