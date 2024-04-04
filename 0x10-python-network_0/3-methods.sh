#!/bin/bash
# Displays all HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep '^Allow:' | sed 's/Allow: //'
