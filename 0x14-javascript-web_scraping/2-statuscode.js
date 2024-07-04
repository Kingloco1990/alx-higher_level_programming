#!/usr/bin/node
const request = require('request');

// Get the URL from command-line arguments
const url = process.argv[2];

// Make an HTTP GET request to the provided URL
request(url, function(error, response) {
    // Check if there's an error during the request
    if (error) {
        console.error(error); // Log the error to the console
    } else {
        // Log the HTTP status code of the response to the console
        console.log(`code: ${response.statusCode}`);
    }
});
