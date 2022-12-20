#!/usr/bin/node

const n = parseInt(process.argv[2], 10);

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x <= 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(n));
