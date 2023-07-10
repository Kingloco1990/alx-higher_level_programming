#!/usr/bin/python3
"""
This module provides a function for converting a class object to a
JSON-compatible dictionary representation.
"""


def class_to_json(obj):
    """
    Convert a class object to a JSON-compatible dictionary representation.

    Args:
        obj (object): The class object to convert.

    Returns:
        dict: A dictionary representing the attributes of the object.
    """
    # Access the dictionary representation of the object's attributes
    obj_dict = obj.__dict__
    return obj_dict

