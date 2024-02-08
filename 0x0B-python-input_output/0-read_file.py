#!/usr/bin/python3
"""
Module: 0-read_file.py

Contains a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function that outputs the contents of a file

    Args:
        filename (str): text file to be printed
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read())
