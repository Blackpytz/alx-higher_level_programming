#!/usr/bin/python3
"""
Module: from_json_string

Contains a function that returns an object (Python data
structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Defines a function takes a single argument
    and returns a JSON string representation

    Args:
        my_str: A JSON serializable object
    """
    return json.loads(my_str)
