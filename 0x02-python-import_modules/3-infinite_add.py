#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_len = len(argv)
    if (arg_len == 1):
        print("0")
    else:
        sum = 0
        for i in range(1, arg_len):
            sum += int(argv[i])
        print("{}".format(sum))
