#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const myObj = {};
    const obj = JSON.parse(body);
    for (i of obj) {
      if (i.completed === true) {
        if (myObj[i.userId] === undefined) {
          myObj[i.userId] = 0;
        }
        myObj[i.userId] += 1;
      }
    }
    console.log(myObj);
  }
});
