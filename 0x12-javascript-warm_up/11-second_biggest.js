#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const my_arg = [];
  let i = 2;
  while (i < process.argv.length) {
    my_arg.push(parseInt(process.argv[i]));
    i++;
  }
  const sorted_args = my_arg.sort((a, b) => (b - a));
  console.log(sorted_args[1]);
}
