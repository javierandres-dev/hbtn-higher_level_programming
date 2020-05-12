#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const apiUrl = process.argv[2];
require('request').get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body).results;
    let times = 0;
    for (let i in obj) {
      let chars = obj[i].characters;
      for (let j in chars) {
        if (chars[j].includes('18')) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
