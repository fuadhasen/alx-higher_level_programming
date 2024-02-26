#!/usr/bin/python3
""" This module provide class Base. """


class Base:
    """ base class defined here. """
    __nb_objects = 0
    def __init__(self, id=None):
        """base class constructor. """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

