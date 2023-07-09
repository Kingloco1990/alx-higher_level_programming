#!/usr/bin/python3
"""
This module provides a function for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to a file specified by the filename.

    Args:
        filename (str, optional): The name of the file to which the text will
                                  be appended. Defaults to "" if not provided.
        text (str, optional): The text to be appended to the file.
                              Defaults to "" if not provided.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf=") as a_file:
        return (a_file.write(text))
