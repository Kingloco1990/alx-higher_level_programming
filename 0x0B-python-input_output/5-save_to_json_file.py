#!/usr/bin/python3
"""
This module provides a function to write Python objects to a text file
using JSON representaiton.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file using JSON representation.

    This function takes a Python object and a filename as input. It
    serializes the object into a JSON string and writes it to the
    specified file.

    Args:
        my_obj (object): The Python object to be saved as JSON.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
