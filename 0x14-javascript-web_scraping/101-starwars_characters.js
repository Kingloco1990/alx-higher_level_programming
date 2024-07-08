#!/usr/bin/node

const request = require('request');

// Function to fetch and print characters sequentially
async function fetchAndPrintCharacters (movieId) {
  try {
    // Construct the URL for the Star Wars API to fetch movie details
    const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

    // Make an HTTP GET request to fetch movie data
    const movieResponse = await new Promise((resolve, reject) => {
      request(apiUrl, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    // Extract characters array from movie response
    const characters = movieResponse.characters;

    // Print each character name sequentially
    for (const characterUrl of characters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(characterResponse);
    }
  } catch (error) {
    console.error('Request failed:', error);
  }
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Call the function to fetch and print characters
fetchAndPrintCharacters(movieId);
