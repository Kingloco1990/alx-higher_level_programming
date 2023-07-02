#!/usr/bin/python3
"""Module for dividing all the elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list): The matrix to be divided. It must be a matrix
                       (list of lists) containing only integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of integers
                   or floats.
        TypeError: If any element in the matrix is not an integer or float.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list: A new matrix with the elements divided by the given divisor.
        The result is rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(element, (int, float)) for row in matrix
                for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
