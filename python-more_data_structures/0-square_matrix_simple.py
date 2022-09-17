#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix=[]
    for i in range(len(matrix)):
        new_list = []
        for j in (matrix[i]):
            j = j * j
            new_list.append(j)
        new_matrix.append(new_list)
    return(new_matrix)
        
