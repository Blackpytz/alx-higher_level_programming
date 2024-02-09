#!/usr/bin/python3
"""
Module: 7-add_item

Contains a script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

"""Check if the file exists"""
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)

"""Add arguments to the list"""
my_list.extend(sys.argv[1:])

"""Save the list to a file"""
save_to_json_file(my_list, filename)
