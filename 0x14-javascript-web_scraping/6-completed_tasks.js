#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTask = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTask[userId]) {
        completedTask[userId] = 0;
      }

      if (completed) ++completedTask[userId];
    }

    console.log(completedTask);
  }
});
