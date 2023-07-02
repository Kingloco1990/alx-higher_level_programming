#!/usr/bin/python3
"""Module for matrix multiplication using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices using NumPy

    Args:
        m_a (ndarray): The first matrix.
        m_b (ndarray): The second matrix.

    Returns:
        ndarray: The result of the matrix multiplication.

    Raises:
        ValueError: If the matrices have incompatible dimensions.
    """
    return (np.matmul(m_a, m_b))
