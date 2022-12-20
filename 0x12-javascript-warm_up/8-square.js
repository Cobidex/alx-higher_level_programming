#!/usr/bin/node

// Write a script that prints a square
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let j = 0;
  while (j < size) {
    let i = 0;
    let row = '';
    while (i < size) {
      row += 'X';
      i++;
    }
    console.log(row);
    j++;
  }
}
