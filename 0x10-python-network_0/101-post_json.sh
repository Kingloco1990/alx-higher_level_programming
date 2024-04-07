#!/bin/bash
# Sends a POST request to a URL (with JSON data) and displays the response body.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
