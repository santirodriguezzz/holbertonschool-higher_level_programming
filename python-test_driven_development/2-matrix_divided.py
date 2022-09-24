#!/usr/bin/python3
def matrix_divided(matrix, div):
    i_num = 0
    for i in matrix:
        if i_num != 0 and len(i) != i_length:
            raise TypeError('Each row of the matrix must have the same size')
        i_length = len(i)
        for item in i:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')     
        i_num += 1
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for i in matrix:
        new_list = []
        for item in i:
            new_list.append(round(item / div, 2))
        new_matrix.append(new_list)
    
    return new_matrix