#!/usr/bin/python3
"""
Module: 8-class_to_json

Contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Defined a function that takes a single argument

    Args:
        obj : An instance of a Class
    """
    return obj.__dict__
