#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  const occurrences = list.reduce((count, element) => {
    // Increment count when the current element matches the searchElement
    // If the current element matches 'searchElement', add 1 to the count; otherwise, add 0
    return count + (element === searchElement ? 1 : 0);
  }, 0);

  // Return the total count of occurrences
  return occurrences;
};
