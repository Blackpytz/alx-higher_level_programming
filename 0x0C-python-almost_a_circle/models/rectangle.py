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
        if not self.__width or not self.__height:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Defines a public method that updates the class Rectangle
        by assigning an argument to each attribute

        Args:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        """
        if args and len(args) > 0:
            # Assign args to attributes in the order they are
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            # Assign kwargs to attributes
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dictionary = {}
        if self.width and self.height and self.x and self.y:
            dictionary['x'] = self.x
            dictionary['y'] = self.y
            dictionary['id'] = self.id
            dictionary['height'] = self.height
            dictionary['width'] = self.width
        return dictionary

    def __str__(self):
        """
        overrides the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        f = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                    self.__y, self.__width,
                                                    self.__height)
        return f
