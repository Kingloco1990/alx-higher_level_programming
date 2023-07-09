#!/usr/bin/python3
"""
This module provides a function for converting a JSON string
to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): A JSON string to be converted.

    Returns:
        object: The Python object resulting from the JSON string.
    """
    return (json.loads(my_str))
