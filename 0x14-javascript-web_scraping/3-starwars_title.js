#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */
const id = process.argv[2];
const apiUrl = 'http://swapi-api.hbtn.io/api/films/';
const endpoint = apiUrl + id;
const req = require('request');
req.get(endpoint, function (err, res, res) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(res);
    console.log(obj.title);
  }
});
