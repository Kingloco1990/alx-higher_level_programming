#!/usr/bin/python3
"""
This module provides a function for adding attributes to objects
dynamically.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to the given object.

    Args:
        obj (object): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        attr_value (any): The value of the attribute.

    Raises:
        TypeError: If the object already has an attribute with the same name.
    """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
