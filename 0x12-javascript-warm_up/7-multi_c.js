#!/usr/bin/node

// Write a script that prints x times “C is fun”
let i = parseInt(process.argv[2], 10);
while (i > 0) {
  console.log('C is fun');
  i--;
}
