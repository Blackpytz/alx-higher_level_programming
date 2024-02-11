#!/usr/bin/python3
"""
Module: base

Contains a class Base
"""


class Base:
    """Defines a class base with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initalizes the Base class and takes a single argument

        Args:
            id (int): A public instance attribute id which is an
            integer
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
