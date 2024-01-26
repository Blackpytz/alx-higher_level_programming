#!/usr/bin/python3
"""
    Creates a class Square that defines a square by:

    * Private instance attribute: size.
    * Private instance atrribute: position.
    * Instantiation with optional size and optional position:
    def __init__(self, size=0, position=(0, 0)).
    * Public instance method: def area(self): that returns the
    current square area.
    * Public instance method: def my_print(self): that prints
    in stdout the square with the character #.
    * Importing any module is not allowed
"""


class Square:
    """Defines a class and instantiate it"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Validate if size attribute is a private instance attribute"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Size must be an integer, otherwise raise a TypeError exception"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """If size is less than 0, raise a ValueError exception"""
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Validate if postion attribute is a private instance attribute"""
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Position must be a tuple of 2 positive integers"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Create a public instance method: def area(self) that returns the
    current square area"""
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
