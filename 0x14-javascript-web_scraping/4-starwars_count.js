#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const request = require('request');
request(process.argv.slice(2)[0], function (error, body) {
  if (error) {
    console.error('error:', error);
  } else {
    let times = 0;
    for (const i of JSON.parse(body.body).results) {
      const character = i.characters;
      for (const j of character) {
        if (j.includes('18')) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
