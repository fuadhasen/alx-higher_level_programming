#!/usr/bin/python3
""" Module provide  class BaseGeometry and subclass rectangle """


class BaseGeometry:
    """ class provide function. """
    def area(self):
        """ function area raise Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate the value. """
        if not isinstance(value, int) or value is True or value is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class that inherited from BaseGeometry parent. """
    def __init__(self, width, height):
        """child class constructor. """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
