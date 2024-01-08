#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        i += 1
    while i > 0:
        print("{}".format(my_list[i - 1]), end="\n")
        i -= 1
