#!/usr/bin/python3
"""
This script sends a GET request to a specified URL and prints the value of
the 'X-Request-Id' header from the response.
"""

import sys
import urllib.request

if __name__ == '__main__':
    # Extract the URL from command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    with urllib.request.urlopen(url) as response:
        # Extract the value of the 'X-Request-Id' header from the response
        x_request_id = dict(response.headers).get('X-Request-Id')

        # Print the value of the 'X-Request-Id' header
        print(x_request_id)
