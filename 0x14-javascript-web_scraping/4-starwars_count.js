#!/usr/bin/node
/* script that prints the number of movies where
the character “Wedge Antilles” is present. */
const rtfm = 'The Force Awakens';
const charId = 18;
const url = 'https://swapi-api.hbtn.io/api/films/';
require('request').get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    let times = 0;
    for (let i of obj.results) {
      for (let j of i.characters) {
        if (j.search(18) > 0) {
          times += 1;
        }
      }
    }
    console.log(times);
  } else {
    console.log(rtfm);
  }
});
