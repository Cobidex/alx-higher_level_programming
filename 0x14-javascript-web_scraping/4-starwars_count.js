#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`status code: ${response.statusCode}`);
    return;
  }
  const res = JSON.parse(body);
  let num = 0;
  for (let i = 0; i < res.length; i++) {
    const characters = res[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const character = character.split('/')[-1];
      if (character === '18') {
        num += 1;
      }
    }
  }
  console.log(num);
});
