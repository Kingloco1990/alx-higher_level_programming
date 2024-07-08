#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL of the Star Wars API for movies using the movieId
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make an HTTP GET request to fetch the movie data from apiUrl
request(apiUrl, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  // Parse the response body as JSON to get movie details
  const movie = JSON.parse(body);

  // Print each character's name who appeared in the movie
  movie.characters.forEach(characterUrl => {
    // Make an HTTP GET request to fetch details of each character
    request(characterUrl, function (error, response, body) {
      // Check if there's an error during the request for character details
      if (error) {
        console.error('Request failed:', error);
        return;
      }

      // Parse the response body as JSON to get character details
      const character = JSON.parse(body);

      // Print the name of the character
      console.log(character.name);
    });
  });
});
