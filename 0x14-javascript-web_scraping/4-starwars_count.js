#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const apiUrl = process.argv[2];
const req = require('request');
const chaId = 18;
let times = 0;
req(apiUrl, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(data);
    const res = obj.results;
    let i = 0;
    let j = 0;
    for (i of res) {
      for (j of i.characters) {
        if (j.includes(chaId)) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
