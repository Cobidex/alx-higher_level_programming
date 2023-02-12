#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (let i = 0; i < characters.length; ++i) {
    request.get(characters[i], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const actor = JSON.parse(body);
      console.log(actor.name);
    });
  }
});
