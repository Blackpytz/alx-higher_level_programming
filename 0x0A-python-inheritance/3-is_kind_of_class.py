#!/usr/bin/python3
"""
Module: 3-is_kind_of_class.py

Contains a function with that checks if the object is
an instance of, or if the object is an instance of a
class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True of False"""
    if isinstance(obj, a_class):
        return True
    return False
