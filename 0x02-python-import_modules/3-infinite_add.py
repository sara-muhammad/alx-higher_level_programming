#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    c = 0
    b = len(argv) - 1
    if b == 0:
        print("0")
    else:
        for i in range(1, len(argv)):
            c = c + int(argv[i])
        print("{}".format(c))
