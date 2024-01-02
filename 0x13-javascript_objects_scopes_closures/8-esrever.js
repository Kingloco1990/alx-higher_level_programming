#!/usr/bin/node

exports.esrever = function (list) {
  // Clone the original list to avoid modifying it
  // Create a new array by slicing the original list
  const reversedList = list.slice();

  // Perform in-place reversal
  // Use a loop to swap elements at positions i and j
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    // Swap elements using destructuring assignment
    [reversedList[i], reversedList[j]] = [reversedList[j], reversedList[i]];
  }

  // Return the reversed list
  return reversedList;
};
