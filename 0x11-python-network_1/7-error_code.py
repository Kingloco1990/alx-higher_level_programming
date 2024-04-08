"""
This script takes in a URL as a command-line argument, sends
a GET request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints
an error message with the status code.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract the URL from the command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        # Print an error message with the status code
        print("Error code:", response.status_code)
    else:
        # Print the body of the response
        print(response.text)
