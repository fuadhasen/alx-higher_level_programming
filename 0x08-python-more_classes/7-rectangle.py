#!/usr/bin/python3
# fuad hassen
# 7-rectangle.py
""" This module define class Rectangle """


class Rectangle:
    """ Rectangle class. """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ intialize constructor.

        Args:
            width (int): frist argument
            height (int): second argument
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """return printable string (#) to the user. """
        if self.__height == 0 or self.__width == 0:
            return ""

        res = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if not isinstance(self.print_symbol, str):
                    res += str(self.print_symbol)
                else:
                    res += self.print_symbol
            if i != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):
        """return official string representation object. """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete the instance and say Bye rectangle... """
        del self.__height
        del self.__width
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
