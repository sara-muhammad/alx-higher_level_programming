#!/usr/bin/python3

if __name__ == "__main__":
    """print the no. and value of CLD"""
    import sys
    argv = sys.argv
    b = len(argv) - 1
    if b == 0:
        print(f"{b} arguments")
    elif b == 1:
        print(f"{b} argument")
        print(f"{b}: {argv[b]}")
    elif b > 1 :
        print(f"{b} arguments")
        for i in range (1, len(argv)):
            print(f"{i}: {argv[i]}")
