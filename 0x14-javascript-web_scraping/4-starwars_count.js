#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';
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
  console.log(res.films.length);
});
