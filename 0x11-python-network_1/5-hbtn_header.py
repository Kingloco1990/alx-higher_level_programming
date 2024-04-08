#!/usr/bin/python3
"""
This script sends a GET request to a specified URL provided as a
command-line argument and prints the value of the
'X-Request-Id' header from the response.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract the URL from the command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Extract the value of the 'X-Request-Id' header from the response
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value of the 'X-Request-Id' header
    print(x_request_id)
