#!/usr/bin/python3

if __name__ == "__main__":
    """update the 1-calculator to receive CLD"""
    import sys
    from calculator_1 import add, mul, sub, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    signs = ["*", "+", "-", "/"]
    argv = sys.argv
    x = int(argv[1])
    y = argv[2]
    z = int(argv[3])
    if y not in signs:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if argv[2] == '+':
            print("{} {} {} = {}".format(x, y, z, add(x, z)))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(x, y, z, mul(x, z)))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(x, y, z, div(x, z)))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(x, y, z, sub(x, z)))