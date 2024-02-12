#!/usr/bin/python3
"""
Module: square

Contains the class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class object"""
        super().__init__(size, size, x, y, id)
        """
        Call the super class constructor with id, x, y, width
        and height. The width and height must be assigned to
        the value of size
        """

    def __str__(self):
        """
        overrides the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>/<size>
        """
        f = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                              self.y, self.width)
        return f
