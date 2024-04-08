#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using
the urllib package.
"""
import urllib.request


if __name__ == '__main__':
    # Specify the URL
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Read the response body
        body = response.read()

        # Decode the response body as UTF-8
        utf8_content = body.decode('utf-8')

        # Display information about the response body
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", utf8_content)
