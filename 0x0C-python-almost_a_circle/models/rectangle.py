#!/usr/bin/python3
"""
Module: rectangle

Contains a class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a class constructor that has five arguments

        Args:
            width (int): An integer variable
            that represents the width of the rectangle
            height (int): An integer variable
            that represents the height of the rectangle
            x (int): An integer variable that represents the x
            coordinate
            y (int): An integer variable that represents the y
            coordinate
            id (int): An integer variable inherited from the super class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        """
        Call the parent class constructor
        """

    @property
    def width(self):
        """Retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with value and type checks"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with value and type checks"""
        if type(value) != int:
            raise TypeError("height  must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrive the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate with value and type checks"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrive the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the width with value and type checks"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("ymust be >= 0")
        self.__y = value

    def area(self):
        """
        Public method that returns the area value of the
        Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance
        with the character #
        """
        for _ in range(self.__height):
            print('#' * self.__width)
