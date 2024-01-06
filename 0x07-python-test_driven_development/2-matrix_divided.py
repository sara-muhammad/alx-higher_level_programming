#!/usr/bin/python3
'''
Define a function for division
'''
def matrix_divided(matrix, div):
    ''' function to divide elements of matrix
    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) and can't be 0
    Raise:
        TypeError if matrix is not list of lists of integers or floats
        TypeError if each row of matrix doesn't have the same size of other rows
        TypeError id div is not integer or float
        ZeroDivisonError if div equal to 0
    Return:
        new matrix with results of division
    '''
    
    if (not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(num, list) for num in matrix)
        or not all((isinstance(elem, int))
                   or (isinstance(elem, float))
                   for elem in [a for b in matrix for a in b])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    if not (all(len(a) == len(matrix[0]) for a in matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if (not (isinstance(div, int) or isinstance(div, float))):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [list(map((lambda x: round(x / div, 2)), row)) for row in matrix]
    return new_matrix

            
    
