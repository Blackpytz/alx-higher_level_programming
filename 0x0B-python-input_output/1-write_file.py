#!/usr/bin/python3
"""
Module: 1-write_file.py

Contains a function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Defines the function that accepts two arguments

    Args:
        filename (txt) : text file to write to
        text (str) : a string of characters to write to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    return (len(text))
