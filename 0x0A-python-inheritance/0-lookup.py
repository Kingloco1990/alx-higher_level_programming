#!/usr/bin/python3
"""Module for object attribute and method lookup."""


def lookup(obj):
    """ Function that lists attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods of
        the object.
    """
    return dir(obj)
