#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const parsedBody = JSON.parse(body);
    const lists = parsedBody.results;

    for (let i = 0; i < lists.length; i++) {
      const charList = lists[i].characters;
      for (let j = 0; j < charList.length; j++) {
        if (charList[j] === charUrl) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
