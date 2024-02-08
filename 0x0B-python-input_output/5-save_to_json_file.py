#!/usr/bin/python3
"""
Module: save_to_json_file

Contains a function that writes an Object to a text
file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that takes two arguments

    Args:
        my_obj (str): A JSON serializable object
        filename: name of the text file
    """
    obj = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(obj)
