#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
const url = args[0];
const filename = args[1];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
