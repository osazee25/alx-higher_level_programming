#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd = []
    for sq in matrix:
        sqrd.append([s**2 for s in sq])
    return sqrd
