#!/usr/bin/python3
""" A class named Square that defines a square by:
    
    * Private instance attribut: size
    * Instantiation with optional size: def __init__(self, size=0):
"""
class Square:
    def __init__(self, size=0):
        try:
            """size must be an integer, and must be greater than 0"""
            if isinstance(size, int) and size >= 0:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
