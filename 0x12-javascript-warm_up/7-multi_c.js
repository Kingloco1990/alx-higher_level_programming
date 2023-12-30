#!/usr/bin/node
const argsNum = parseInt(process.argv[2]);
let counter = 0;

if (isNaN(argsNum)) {
  console.log('Missing number of occurrences');
}
while (counter < argsNum) {
  console.log('C is fun');
  counter++;
}
