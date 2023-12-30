#!/usr/bin/node
const size = parseInt(process.argv[2]);
let yCounter = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (yCounter < size) {
    let line = '';
    for (let xCounter = 0; xCounter < size; xCounter++) {
      line += 'X';
    }
    console.log(line);
    yCounter++;
  }
}
