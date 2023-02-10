#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (error, response, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const chars = body[i].chars;

    for (let j = 0; j < chars.length; ++j) {
      const chars = chars[j];
      const charsId = chars.split('/')[5];

      if (charsId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
