#!/usr/bin/python3
"""
Module: base

Contains a class Base
"""
import json


class Base:
    """Defines a class base with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initalizes the Base class and takes a single argument

        Args:
            id (int): A public instance attribute id which is an
            integer
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        Otherwise return the string "[]"

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
