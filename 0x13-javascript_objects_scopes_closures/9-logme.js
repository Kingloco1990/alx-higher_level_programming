#!/usr/bin/node

// Initialize a counter for the number of arguments printed
let argsPrinted = 0;

exports.logMe = function (item) {
  // Log the number of arguments already printed and the current argument value
  console.log(`${argsPrinted}: ${item}`);

  // Increment the counter after printing each argument
  argsPrinted++;
};
