#!/usr/bin/node

const firstArg = process.argv[2];
function fact (num1) {
  const num = parseInt(num1);
  if (isNaN(num) || num === 0 || num === 1) {
    return 1;
  } else {
    return (num * fact(num - 1));
  }
}

const res = fact(firstArg);
console.log(res);
