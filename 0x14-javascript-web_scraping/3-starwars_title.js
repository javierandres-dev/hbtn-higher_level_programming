#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */
const movieId = process.argv[2];
const apiUrl = 'http://swapi-api.hbtn.io/api/films/';
const endpoint = apiUrl + movieId;
const req = require('request');
req.get(endpoint, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(data);
    console.log(obj['title']);
  }
});
