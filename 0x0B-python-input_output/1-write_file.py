#!/usr/bin/python3
"""
This module provides a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Args:
        filename (str, optional): The name of the file to write to.
        If not provided, an empty string is used.
        text (str, optional): The text to write to the file.
        If not provided, an empty string is used.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return (a_file.write(text))
