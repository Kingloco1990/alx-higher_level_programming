#!/usr/bin/python3
"""
This script takes a GitHub username and personal access token
as command-line arguments,sends a GET request to the
GitHub API using Basic Authentication, and displays the user id
if the request is successful. If the request is not successful,
it displays None.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract GitHub username and personal access token
    # from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Set up the URL for the GitHub API
    url = 'https://api.github.com/user'

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Display the user id
        print(response.json()['id'])
    else:
        # Display None if the request was not successful
        print(None)
