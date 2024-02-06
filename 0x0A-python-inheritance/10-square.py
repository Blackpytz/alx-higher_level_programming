#!/usr/bin/python3
"""
Module: 8-rectangle.py

Contains a class Square that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Defines a Square class"""
    def __init__(self, size):
        """
        Initializes a square object with size attribute

        Args:
            size (int): The size of the square
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
