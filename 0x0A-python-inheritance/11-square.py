#!/usr/bin/python3
""" Module provide  class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherited from Rectangle parent. """
    def __init__(self, size):
        """child class constructor. """
        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        """ implement the area by overriding parent area'"""
        return self.__size * self.__size

    def __str__(self):
        """return string representstiion of the object. """
        return "[Square] {}/{}".format(self.__size, self.__size)
