#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  console.log(num1 + num2);
}

add(firstArg, secondArg);
