#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        res.append([e**2 for e in i])
    return res
