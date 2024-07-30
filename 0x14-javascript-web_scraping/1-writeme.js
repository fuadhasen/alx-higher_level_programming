#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const content = args[1];

fs.writeFile(args[0], content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
