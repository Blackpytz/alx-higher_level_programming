#!/usr/bin/python3
"""
Module: load_from_json_file

Contains a function that creates an Object from
a "JSON file"
"""
import json


def load_from_json_file(filename):
    """
    Defines a function that takes a single argument

    Args:
        filename (json): A json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
