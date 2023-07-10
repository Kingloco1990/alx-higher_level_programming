#!/usr/bin/python3
"""
This module generates a Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a given number of rows.

    Args:
         n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: Pascal's triangle as a list of lists representing rows.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
