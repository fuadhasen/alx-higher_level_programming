#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(`code: ${error.message}`);
  } else {
    const parsedBody = JSON.parse(body);
    console.log(`${parsedBody.title}`);
  }
});
