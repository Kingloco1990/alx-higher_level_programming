#!/usr/bin/python3
"""
This module allows you to add all arguments to a Python list and save
to a file using JSON representation.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    arguments = sys.argv[1:]

    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []
    existing_list.extend(arguments)
    save_to_json_file(existing_list, "add_item.json")
