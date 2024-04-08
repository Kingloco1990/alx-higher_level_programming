#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter
provided as a command-line argument and prints the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send a POST request to the specified URL with the email as a parameter
    response = requests.post(url, data={'email': email})

    # Print the body of the response
    print(response.text)
