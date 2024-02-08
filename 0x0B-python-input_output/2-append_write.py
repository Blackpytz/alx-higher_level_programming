#!/usr/bin/python3
"""
Module: 2-append_write.py

Contains a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Defines a function that takes two arguments
    
    Args:
        filename (txt): name of the file to append to
        text (str): string of characters to append to the txt file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)

    return len(text)
