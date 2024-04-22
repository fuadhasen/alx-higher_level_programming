#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let r = '';
    for (let j = 0; j < num; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
