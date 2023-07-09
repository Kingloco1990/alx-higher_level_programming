#!/usr/bin/python3
"""
Summary
"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    with open(filename, "r") as a_file:
        json.loads(a_file)
