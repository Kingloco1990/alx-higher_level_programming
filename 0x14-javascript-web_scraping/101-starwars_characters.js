#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API to fetch movie details
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make an HTTP GET request to fetch movie data
request(apiUrl, function (error, response, body) {
  // Handle request errors
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body);

  // Print each character name in the order they appear in the movie's characters list
  movie.characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      // Handle request errors for character details
      if (error) {
        console.error('Request failed:', error);
        return;
      }

      // Parse the character details as JSON
      const character = JSON.parse(body);

      // Print the name of the character
      console.log(character.name);
    });
  });
});
