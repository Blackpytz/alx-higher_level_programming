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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Defines a public method that updates the class Rectangle
        by assigning an argument to each attribute

        Args:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
        """
        if args and len(args) > 0:
            # Assign args to attributes in the order they are
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            # Assign kwargs to attributes
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """
        overrides the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>/<size>
        """
        f = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                              self.y, self.width)
        return f
