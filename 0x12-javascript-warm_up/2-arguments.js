#!/usr/bin/node

const arr = process.argv;
if (arr.length === 2) {
  console.log('No argument');
} else if (arr.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
