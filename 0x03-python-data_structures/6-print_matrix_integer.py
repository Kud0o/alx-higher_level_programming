#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            if i:
                print("{}".format(''.join("{:d}" for j in i[:-1]), end=' ') + "{}".format(f"{i[-1]}", end=''))
    
