#!/usr/bin/python3
# fuad hassen
# 2-matrix_divided.py
"""this module provide function that divide a matrix"""


def matrix_divided(matrix, div):
    """matrix divide.

    Args:
        matrix (list of list): matrix.
        div (int): divider.

    Returns:
        new_matrix (list): new matrix.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(0, len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, float):
        div = int(div)
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    sub = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            res = matrix[i][j] / div
            res = round(res, 2)
            sub.append(res)
            if len(sub) == len(matrix[0]):
                new_matrix.append(sub)
                sub = []

    return new_matrix
