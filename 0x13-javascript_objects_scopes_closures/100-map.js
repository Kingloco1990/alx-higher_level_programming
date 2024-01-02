#!/usr/bin/node

// Import the 'list' array from the file 100-data.js
const list = require('./100-data').list;

// Uses the map function to create a new list where each value is multiplied by its index
const newList = list.map(function (num, index) {
  return num * index;
});

// Prints the initial list
console.log(list);

// Prints the new list
console.log(newList);
