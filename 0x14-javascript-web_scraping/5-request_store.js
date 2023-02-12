#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Error: status code is ${response.statusCode}`);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (error) {
      console.log('Error Writing to File');
    }
  });
});
