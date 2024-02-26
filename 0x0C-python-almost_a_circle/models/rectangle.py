#!/usr/bin/python3
"""This module provide Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """Reectangle class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width. """
        return self.__width

    @width.setter
    def width(self, width):
        """setter of width."""
        self.__width = width

    @property
    def height(self):
        """getter of height. """
        return self.__height

    @height.setter
    def height(self, height):
        """setter of height."""
        self.__height = height

    @property
    def y(self):
        """getter of y. """
        return self.__y

    @y.setter
    def y(self, y):
        """setter of y."""
        self.__y = y

    @property
    def x(self):
        """getter of x. """
        return self.__x

    @x.setter
    def x(self, x):
        """setter of x."""
        self.__x = x
