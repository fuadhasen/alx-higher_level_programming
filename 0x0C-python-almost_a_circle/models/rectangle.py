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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter of height. """
        return self.__height

    @height.setter
    def height(self, height):
        """setter of height."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def y(self):
        """getter of y. """
        return self.__y

    @y.setter
    def y(self, y):
        """setter of y."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        """getter of x. """
        return self.__x

    @x.setter
    def x(self, x):
        """setter of x."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def area(self):
        """compute the area. """
        return self.__width * self.__height

    def display(self):
        """display the rectangle. """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation. """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
