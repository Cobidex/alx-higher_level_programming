#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const users = JSON.parse(body);
  const myDict = {};
  for (let i = 0; i < users.length; ++i) {
    let temp = 1;
    if (temp === users[i].userId) {
      if (users[i].completed) {
        if (temp in myDict) {
          myDict[temp] += 1;
        } else {
          myDict[temp] = 1;
        }
      } else {
        if (!(temp in myDict)) {
          myDict[temp] = 0;
        }
      }
    } else {
      if (users[i].completed) {
        temp = users[i].completed;
        if (temp in myDict) {
          myDict[temp] += 1;
        } else {
          myDict[temp] = 1;
        }
      } else {
        if (!(temp in myDict)) {
          myDict[temp] = 0;
        }
      }
    }
  }
  console.log(myDict);
});
