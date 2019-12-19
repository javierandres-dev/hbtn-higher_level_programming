#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        square = list(map(lambda n: n * n, i))
        result.append(square)
    return (result)
