#!/usr/bin/python3
"""Creates a class Square that defines a square by:

    * Private instance attribute; size
    * Private instance atrribute: Position
"""


class Square:
    """Square instantiated with the optional size and optional position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Create a private instance attribute size"""
    @property
    def size(self):
        return self.__size

    """Validate if it is private using property setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Create a private instance attribute position"""
    @property
    def position(self):
        return self.__position

    """Validate if it is private using property setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    """def area - a public instance method that returns the
        current square area"""
    def area(self):
        return self.__size ** 2

    """def my_print - a public instance method that prints in stdout the square
        with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        result = ""
        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip()
