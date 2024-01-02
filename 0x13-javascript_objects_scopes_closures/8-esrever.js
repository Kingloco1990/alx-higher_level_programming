#!/usr/bin/node

exports.esrever = function (list) {
  // Clones the original list to avoid modifying it
  // Creates a new array by slicing the original list
  const reversedList = list.slice();

  // Performs in-place reversal
  // Uses a loop to swap elements at positions i and j
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    // Swaps elements using destructuring assignment
    [reversedList[i], reversedList[j]] = [reversedList[j], reversedList[i]];
  }

  // Returns the reversed list
  return reversedList;
};
