#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const myArg = [];
  let i = 2;
  while (i < process.argv.length) {
    myArg.push(parseInt(process.argv[i]));
    i++;
  }
  const sortedArgs = myArg.sort((a, b) => (b - a));
  console.log(sortedArgs[1]);
}
