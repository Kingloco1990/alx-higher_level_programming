#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using
the the requests package.
"""

import requests

if __name__ == '__main__':
    # Send a GET request to the specified URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Display information about the response body
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
