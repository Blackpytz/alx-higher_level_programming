#!/usr/bin/python3
"""
Module: 1-my_list.py

Contains a class MyList that inherits from list
"""


class MyList(list):
    """Defined MyList class"""
    def print_sorted(self):
        """
        Public instance method that prints
        the list, but sorted (ascending sort)
        """
        print(sorted(self))
