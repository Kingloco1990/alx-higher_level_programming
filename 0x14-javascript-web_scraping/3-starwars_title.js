#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments (third argument)
const movieId = process.argv[2];

// Construct the URL for the Star Wars API using the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the provided URL
request(url, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    // Log the error to the console and exit the callback function
    console.error('Request failed:', error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Check if the response data contains the movie title
  if (data.title) {
    // Log the movie title to the console
    console.log(data.title);
  } else {
    // Log an error message with the status code if the title is not found
    console.error('Error code:', response.statusCode);
  }
});
