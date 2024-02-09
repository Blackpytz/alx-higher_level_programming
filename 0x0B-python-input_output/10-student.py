#!/usr/bin/python3
"""
Module: 10-student

Contains a class Student
"""


class Student:
    """Defines a class Student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student object

        Args:
            first_name (str): a string variable
            last_name (str): a stiring variable
            age (int): an int variable
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Defines a public method that retrieves a dictionary
        representation of a Student instance
        """
        json_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        json_new_data = {}
        if isinstance(attrs, list):
            for key in json_data:
                for attr in attrs:
                    if attr in json_data:
                        json_new_data[attr] = json_data[attr]
            return json_new_data
        else:
            return json_data
