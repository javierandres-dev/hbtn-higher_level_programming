def matrix_divided(matrix, div):
    new_matrix = []
    tmp = []
    for i in matrix:
        tmp = list(map(lambda x: round(x / div, 2), i))
        new_matrix.append(tmp)
    return new_matrix
