#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix. """
    new_matrix = []
    tmp = []
    size = len(matrix[0])
    for i in range(len(matrix)):
        if size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for j in matrix:
        for k in j:
            if type(k) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
        tmp = list(map(lambda x: round(x / div, 2), j))
        new_matrix.append(tmp)
    return new_matrix
