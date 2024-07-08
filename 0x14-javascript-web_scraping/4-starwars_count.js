#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command-line arguments (third argument)
const apiUrl = process.argv[2];

// Make an HTTP GET request to the provided API URL
request(apiUrl, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    // Log the error to the console and exit the callback function
    console.error('Request failed:', error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Check if the response contains films
  if (data.results) {
    // Filter the films to count how many include the character "Wedge Antilles" (character ID 18)
    const count = data.results.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;

    // Log the count to the console
    console.log(count);
  } else {
    // Log an error message if no films are found
    console.error('No films found');
  }
});
