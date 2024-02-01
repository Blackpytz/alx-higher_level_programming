#!/usr/bin/python3
"""Create a class Rectangle"""


class Rectangle:
    """Defines a rectangle class
    Args:
        @width - width of the rectangle
        @height - height of the rectangle
    Raises:
        TypeError - if value is not an integer
        ValueError - if value is less than 0
    """
    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width attribute"""
        return self.__width

    @property
    def height(self):
        """Retrieve the height attribute of the class Rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width with value and type checks"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """Returns the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += '#' * self.__width + '\n'

        return rectangle.rstrip()

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of rectangle and print message
        'Bye rectangle...'"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
