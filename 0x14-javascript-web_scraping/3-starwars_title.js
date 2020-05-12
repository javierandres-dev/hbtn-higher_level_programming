#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */
const id = process.argv[2];
const apiUrl = 'http://swapi-api.hbtn.io/api/films/';
const endpoint = apiUrl + id;
const req = require('request');
req.get(endpoint, function (err, res, data) {
  if (err === null) {
    const obj = JSON.parse(data);
    console.log(obj.title);
  }
});
