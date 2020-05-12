#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const apiUrl = process.argv[2];
const request = require('request')
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const obj = JSON.parse(body);
    let times = 0;
    for (let i of obj.results) {
      for (let j of i.characters) {
        if (j.indexOf('/18/') > 0) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
