#!/usr/bin/python3
"""
Module: 6-base_geometry.py

Contains a class BaseGeometry
"""


class BaseGeometry:
    """Defines a class called BaseGeometry"""
    def area(self):
        """
        raises an Exception with message
        'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
