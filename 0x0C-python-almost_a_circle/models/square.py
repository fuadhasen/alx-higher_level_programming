#!/usr/bin/python3
""" This module provide class Square. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square subclass of Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ subclass constructor. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter of size. """
        return self.width

    @size.setter
    def size(self, size):
        """ setter. """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """overriding the str. """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
