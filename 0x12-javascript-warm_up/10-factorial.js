#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = parseInt(args[0]);

function fact (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

const res = fact(num1);
console.log(res);
