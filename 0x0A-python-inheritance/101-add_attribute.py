#!/usr/bin/python3
"""
Module: 101-add_attribute.py

Contains a function that adds a new attribute to an
object if it's possible
"""
def add_attribute(obj, attr, value):
    """Define function"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    
    obj.__dict__[attr] = value
