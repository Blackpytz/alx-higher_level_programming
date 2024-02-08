#!/usr/bin/python3
"""
Module: to_json_string

Contains a function that returns the JSON representation
of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Defines a function that converts an object and returns
    the JSON representation.

    Args:
        my_obj (Any): A JSON serializable object
    """
    return json.dumps(my_obj)
