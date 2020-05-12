#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */
const id = process.argv[2];
const api = 'http://swapi-api.hbtn.io/api/films/';
const endpoint = api + id;
const req = require('request');
req(endpoint, function (err, res, data) {
  if (err === null) {
    const obj = JSON.parse(data);
    console.log(obj.title);
  }
});
