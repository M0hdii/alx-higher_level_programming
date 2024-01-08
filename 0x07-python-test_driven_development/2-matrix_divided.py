#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div equals to 0.

    Returns:
        A new matrix representing the result of the division.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if type(matrix[0]) is list:
        starting_lenght = len(matrix[0])

    for L in matrix:
        if type(L) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(L) != starting_lenght:
            raise TypeError("Each row of the matrix must \
have the same size")
        for n in L:
            if type(n) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    new_list = []
    new_matrix = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for L in matrix:
        for n in L:
            new_list.append(round((n / div), 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
