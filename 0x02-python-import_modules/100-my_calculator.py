#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argument_count = len(sys.argv)
    if argument_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    operator = sys.argv[2]
    num2 = int(sys.argv[3])

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = sub(num1, num2)
    elif operator == '*':
        result = mul(num1, num2)
    elif operator == '/':
        result = div(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(num1, operator,mnum2, result))
