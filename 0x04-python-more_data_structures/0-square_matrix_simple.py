#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    F = []
    TMP = []
    for i in range(len(matrix)):
        TMP = list(map(lambda x: x ** 2, matrix[i]))
        F.append(TMP)
    return F
