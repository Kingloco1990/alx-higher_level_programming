#!/usr/bin/node

const { dict } = require('./101-data');

// Creates a new dictionary to store user ids by occurrence
const resultDict = {};

// Iterates through the keys of the original dictionary
for (const userId in dict) {
  // Gets the number of occurrences from the original dictionary
  const occurrences = dict[userId];

  // If the occurrences is not a key in the result dictionary, initialize it as an empty array
  if (!resultDict[occurrences]) {
    resultDict[occurrences] = [];
  }

  // Pushes the user id to the array corresponding to the number of occurrences
  resultDict[occurrences].push(userId);
}

// Prints the new dictionary
console.log(resultDict);
