#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let y = 0; y < num; y++) {
      str += 'X';
    }
    console.log(str);
  }
}
