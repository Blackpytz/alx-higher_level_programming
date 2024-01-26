#!/usr/bin/python3
""" A class named Square that defines a square by:

    * Private instance attribut: size
    * Instantiation with optional size: def __init__(self, size=0):
"""


class Square:
    """Class Square is defined"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size must be an integer"""
        if not isinstance(value, int):
            """raise a TypeError exception"""
            raise TypeError("size must be an integer")

        if value < 0:
            """ raise a ValueError exception"""
            raise ValueError("size must be >= 0")

        self.__size = value
