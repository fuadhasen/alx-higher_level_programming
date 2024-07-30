#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];

request(url, function (error, response) {
  if (error) {
    console.error(`code: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
