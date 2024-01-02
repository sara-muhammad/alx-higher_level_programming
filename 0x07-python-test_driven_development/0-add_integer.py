#!/usr/bin/python3
'''
Define a function for Addition
'''
def add_integer(a, b=98):
    ''' function to add two integers or floats 
    Args:
        a: first number
        b: second number pre-set to 98
    Raise:
        TypeError if a or b is not integer or float
    Return:
        The sum of a and b as integer
    '''
    if (not (isinstance(a, int) or isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not (isinstance(b, int) or isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int (b))
