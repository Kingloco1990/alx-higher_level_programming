#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const numA = parseInt(process.argv[2]);
const numB = parseInt(process.argv[3]);

if (isNaN(numA) || isNaN(numB)) {
  console.log('NaN');
} else {
  console.log(add(numA, numB));
}
