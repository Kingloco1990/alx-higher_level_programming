#!/bin/bash
# Displays the response body after sending a GET request with a header variable to a URL.
curl -sH "X-School-User-Id: 98" "$1"
