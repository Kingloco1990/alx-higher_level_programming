#!/usr/bin/python3
"""Module for printing a square with the character #"""


def print_square(size):
    """Function that prints a square using the character #.

    Args:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If the input size is not an integer.
        ValueError: If the input size is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
