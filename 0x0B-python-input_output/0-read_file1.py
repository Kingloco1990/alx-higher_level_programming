#!/usr/bin/python3
"""
This module provides a function for file operations.
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str, optional): The name of the file to be read.
        Defaults to "".
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")


read_file("my_file_0.txt")
