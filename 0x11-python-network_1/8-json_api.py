#!/usr/bin/python3
"""
This script takes a single letter as a command-line argument,
sends a POST request to http://0.0.0.0:5000/search_user with the letter
as a parameter, and displays the id and name from the JSON response.
If no letter is provided or the JSON response is empty, it displays
'No result'. If the JSON response is not properly formatted, it displays
'Not a valid JSON'.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract the letter from the command-line arguments
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send a POST request to the specified URL with the letter as a parameter
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        # Convert response to JSON format
        json_response = res.json()

        # Check if JSON is properly formatted and not empty
        if json_response:
            # Display id and name from the response
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            # Display 'No result' if JSON is empty
            print("No result")
    except ValueError:
        # Display 'Not a valid JSON' if JSON is invalid
        print("Not a valid JSON")
