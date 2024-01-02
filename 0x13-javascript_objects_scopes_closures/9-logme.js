#!/usr/bin/node

// Initializes a counter for the number of arguments printed
let argsPrinted = 0;

exports.logMe = function (item) {
  // Logs the number of arguments already printed and the current argument value
  console.log(`${argsPrinted}: ${item}`);

  // Increments the counter after printing each argument
  argsPrinted++;
};
