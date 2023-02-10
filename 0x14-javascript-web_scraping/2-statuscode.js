#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (ero, res) {
  console.log('code:', res.statusCode); // Print response status code if response was received
});
