#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const completeTask = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const parsedBody = JSON.parse(body);
    parsedBody.forEach(task => {
      if (task.completed === true) {
        if (!completeTask[task.userId]) {
          completeTask[task.userId] = 0;
        }
        completeTask[task.userId]++;
      }
    });
  }
  console.log(completeTask);
});
