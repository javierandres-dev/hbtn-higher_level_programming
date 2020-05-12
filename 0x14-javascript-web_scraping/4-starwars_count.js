#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const charId = 18;
const request = require('request')
request(process.argv.slice(2)[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    let times = 0;
    for (let i of obj.results) {
      for (let j of i.characters) {
        if (j.includes(charId)) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
