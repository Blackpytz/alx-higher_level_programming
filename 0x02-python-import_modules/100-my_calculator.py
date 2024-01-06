#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argument_count = len(sys.argv)
    if argument_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif operator == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num1)))
    elif operator == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif operator == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
