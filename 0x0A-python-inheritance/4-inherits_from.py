#!/usr/bin/python3
"""
Module: 3-is_kind_of_class.py

Contains a function with that checks if the object is
an instance of, or if the object is an instance of a
class that inherited (directly or indirectly)from, the specified class
"""


def inherits_from(obj, a_class):
    """Returns True of False"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
