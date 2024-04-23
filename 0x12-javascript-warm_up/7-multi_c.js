#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
