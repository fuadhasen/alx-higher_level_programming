#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.error(`code: ${error.message}`);
  } else {
    const parsedBody = JSON.parse(body);
    const lists = parsedBody.results;
    let count = 0;

    for (let i = 0; i < lists.length; i++) {
      const charList = lists[i].characters;
      for (let j = 0; j < charList.length; j++) {
        if (charList[j] === charUrl) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
