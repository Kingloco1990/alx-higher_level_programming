#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make an HTTP GET request to the provided URL
request(url, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  // Attempt to write the response body to the specified file
  fs.writeFile(filePath, body, 'utf8', function (err) {
    // Log only if there is an error during the file write operation
    if (err) {
      console.error('Failed to write to file:', err);
    }
  });
});
