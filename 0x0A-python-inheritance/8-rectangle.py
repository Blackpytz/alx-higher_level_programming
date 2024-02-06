#!/usr/bin/python3
"""
Module: 8-rectangle.py

Contains a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle"""
    def __init__(self, width, height):
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
