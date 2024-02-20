#!/usr/bin/python3
""" Module provide  class BaseGeometry. """


class BaseGeometry:
    """ class provide function. """
    def area(self):
        """ function area raise Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate the value. """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
