#!/usr/bin/python3
"""Creates a python class Square that defines a square by:

    * Private instance atrribute: size:
        - property def size(self): to retrive it
        - property setter def size(self, value) to set it:
    * Instantiation with optional size: def __init__(self, size=0):
    * Public instance method: def area(self): that returns the
    current square area
    * Public instance method: def my_print(self): that prints in
    stdout the square with the character #
        * if size is equal to 0, print an empty line
"""


class Square:
    """Class defined and instantiated"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
