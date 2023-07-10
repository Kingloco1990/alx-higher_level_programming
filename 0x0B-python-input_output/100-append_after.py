#!/usr/bin/python3
"""
This module provides a function that appends a new string after
a specified search string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after a specified search string in a file.

Args:
    filename (str, optional): The name of the file to modify.
                            Defaults to an empty string.
    search_string (str, optional): The string to search for in the file.
                                   Defaults to an empty string.
    new_string (str, optional): The string to append after the search string.
                                Defaults to an empty string.
    """

    # Read the contents of the file
    text = ""
    with open(filename) as r_file:
        for line in r_file:
            text += line
            if search_string in line:
                text += new_string

    # Write the modified contents back to the file
    with open(filename, "w") as w_file:
        w_file.write(text)
