#!/usr/bin/node
function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}

console.log(factorial(parseInt(process.argv[2])));
