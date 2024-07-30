#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const charUrl = '18';
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const parsedBody = JSON.parse(body);
    const lists = parsedBody.results;

    lists.forEach(item => {
      item.characters.forEach(Actors => {
        if (Actors.includes(charUrl)) {
          count += 1;
        }
      });
    });
  }
  console.log(count);
});
