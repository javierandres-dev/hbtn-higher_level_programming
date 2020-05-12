#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const endpoint = url + id;
const req = require('request');
req.get(endpoint, function (err, res, data) {
  let code = res.statusCode;
  if (code === 200) {
    const obj = JSON.parse(data);
    console.log(obj.title);
  }
  if (err) {
    console.log(err);
  }
});
