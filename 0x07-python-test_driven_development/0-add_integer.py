#!/usr/bin/python3
"""Module for adding numbers"""


def add_integer(a, b=98):
    """
    Function that adds two numbers and returns their sum as an integer.

    Parameters:
        a (int or float): The first operand of the addition operation.
        b (int or float, optional): The second operand of the addition
                                    operation. Defaults to 98.

    Returns:
        The return value. a + b

    Raises:
        TypeError: If 'a' or 'b' is not an integer or a float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
