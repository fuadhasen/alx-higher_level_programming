#!/usr/bin/python3
""" Module provide  class BaseGeometry and subclass rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherited from BaseGeometry parent. """
    def __init__(self, width, height):
        """child class constructor. """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ implement the area by overriding parent area'"""
        return self.__width * self.__height

    def __str__(self):
        """ string representation. """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
