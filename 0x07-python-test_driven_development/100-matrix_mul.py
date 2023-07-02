#!/usr/bin/python3
"""Module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the result.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list,
            or if any element in `m_a`
            or `m_b` is not an integer or a float,
            or if the rows of `m_a`
            or `m_b` have varying sizes.

        ValueError: If `m_a` or `m_b` is empty.
    """
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list) or not all(isinstance(row, list)
                                            for row in m_a):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list) or not all(isinstance(row, list)
                                            for row in m_b):
        raise TypeError("m_b must be a list")

    if not all(isinstance(element, (int, float)) for row in m_a
               for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float)) for row in m_b
               for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
