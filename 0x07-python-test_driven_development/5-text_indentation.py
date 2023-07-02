#!/usr/bin/python3
"""Module for adding indentation to a given text string"""


def text_indentation(text):
    """Function for formatting a text by adding two new lines after
       each occurrence of '.', '?', and ':'

    Args:
        text (str): The text string to be indented.

    Raises:
        TypeError: If the input 'text' is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that require new lines
    newline_chars = [".", "?", ":"]

    # Initialize an empty string to store the indented text
    indented_text = ""

    # Iterate over each character in the text
    for char in text:
        # Add the character to the indented text
        indented_text += char

        # Add 2 new lines after specific characters
        if char in newline_chars:
            indented_text += "\n\n"

    # Print the indented text without leading or trailing spaces
    print(indented_text.strip())
