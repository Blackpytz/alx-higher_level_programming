#!/usr/bin/python3
"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """Instantiate with optional width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Use the @property decorator to transform the attribute
        into a read-only property"""
    @property
    def width(self):
        return self.__width

    """Use the @setter decorator to transform the attribute
        into a setter method"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Use the @property decorator to transform the attribute
        into a read-only property"""
    @property
    def height(self):
        return self.__height

    """Use the @setter decorator to transform the attribute
        into a setter method"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
