#!/usr/bin/node
// Check if the number of command line arguments is less than or equal to 3
if (process.argv.length <= 3) {
  // If so, print 0 and exit the script
  console.log(0);
} else {
  // If there are more than 3 command line arguments
  // Map the command line arguments to Numbers
  const args = process.argv.map(Number)
    // Slice the array to exclude the first two elements (script name and interpreter)
    .slice(2, process.argv.length)
    // Sort the array in ascending order
    .sort((a, b) => a - b);

  // Print the second-to-last element of the sorted array
  console.log(args[args.length - 2]);
}
