#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argument_count = len(sys.argv)
    if argument_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    print("{}".format(operator))
    if operator != '+' and '-' and '*' and '/':
        print("Unknown operator. Available operators: +, -, * and /")