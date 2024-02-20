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
