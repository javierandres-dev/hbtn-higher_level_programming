#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const charId = 18;
const url = 'https://swapi-api.hbtn.io/api/films/';
require('request').get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    let times = 0;
    for (let i of obj.results) {
      for (let j of i.characters) {
        if (j.search(charId) > 0) {
          times++;
        }
      }
    }
    console.log(times);
  }
});
