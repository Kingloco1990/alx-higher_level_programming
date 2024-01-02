#!/usr/bin/node

exports.converter = function (base) {
  // Inner function takes a 'number' as an argument
  return function (number) {
    // The toString method with the specified base to converts the number
    return number.toString(base);
  };
};
