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
    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with
            width == height == size

        Args:
            size (int): size of the new rectangle height and width"""
        return (cls(size, size))

    def __str__(self):
        """Returns the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            try:
                rectangle += str(self.print_symbol) * self.__width + '\n'
            except Exception:
                rectangle += type(self).print_symbol
        return rectangle.rstrip('\n')

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of rectangle and print message
        'Bye rectangle...'"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
