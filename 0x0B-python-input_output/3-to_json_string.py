#!/usr/bin/python3
"""
This module provides a function to convert Python objects to JSON strings.
"""
import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string representation.

    Args:
        my_obj (object): The Python object to be converted.

    Returns:
        str: The JSON string representation of the given object.
    """
    return json.dumps(my_obj)
