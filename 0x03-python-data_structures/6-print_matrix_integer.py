#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            if len(i) > 0:
                print("{}".format(''.join(f"{j} " for j in i[:-1]), end='') + f"{i[-1]}")
    
