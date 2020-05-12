#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const apiUrl = process.argv[2];
const req = require('request');
req(apiUrl, function (err, res, data){
  if (err) {
    console.log(err);
  } else {
    const myObj = {};
    const obj = JSON.parse(data);
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
