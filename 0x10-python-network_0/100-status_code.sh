#!/bin/bash
# Sends a GET request a URL passed as an argument and displays the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
