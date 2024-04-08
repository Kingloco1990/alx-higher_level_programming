#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter,
and displays the body of the response after decoding it using UTF-8.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email address as a URL parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request object with the URL and encoded data
    request = urllib.request.Request(url, data=data)

    # Send the POST request and handle the response
    with urllib.request.urlopen(request) as response:
        # Read the response body and decode it using UTF-8
        content = response.read().decode('utf-8')

        # Display the decoded content
        print(content)
