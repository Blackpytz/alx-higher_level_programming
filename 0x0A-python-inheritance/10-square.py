#!/usr/bin/python3
"""
Module: 8-rectangle.py

Contains a class Square that inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size):
        """
        Initializes a square object with size attribute

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        """
        Call the parent class constructor
        with size as both width and height
        """
        self.__size = size
