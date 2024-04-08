#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). It handles urllib.error.HTTPError exceptions
and prints the corresponding HTTP status code in case of an error.
"""

import urllib.error
import urllib.request
import sys

if __name__ == '__main__':
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code:", e.code)
