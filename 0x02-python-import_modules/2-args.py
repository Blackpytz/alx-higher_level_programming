#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_len = len(argv)
    if arg_len == 1:
        print("0 arguments")
    else:
        print("{} arguments:".format(int(arg_len) - 1))
        for i in range(1, arg_len):
            print("{}: {}".format(i, argv[i]))
