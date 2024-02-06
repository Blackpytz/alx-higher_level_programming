#!/usr/bin/python3
"""
Module: 100-my_int.py

Contains a class MyInt that inherits from int
"""

class MyInt(int):
    """Define MyInt class"""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
