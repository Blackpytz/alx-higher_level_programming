#!/usr/bin/python3
def number_keys(a_dictionary):
    number_keys = 0
    for i in a_dictionary.items():
        number_keys += 1

    return number_keys
