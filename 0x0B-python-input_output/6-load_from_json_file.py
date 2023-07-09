#!/usr/bin/python3
"""
This module provides functions for working with JSON files.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict or list: The loaded data as a dictionary or list, depending
        on the structure of the JSON file.
    """
    with open(filename) as a_file:
        return json.load(a_file)
