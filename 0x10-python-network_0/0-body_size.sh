#!/bin/bash
# Displays the size of the body of an HTTP response by using a URL.
curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}'
