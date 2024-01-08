#!/usr/bin/python3
""" This module define print_square """
def print_square(size):
    """ function to print square with # 
    Args:
        
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end= "")
        print('\n')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
