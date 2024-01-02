#!/usr/bin/node

// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define the Square class that inherits from Rectangle
module.exports = class Square extends Rectangle {
  // Constructor for Square
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) using super()
    super(size, size);
  }
};
