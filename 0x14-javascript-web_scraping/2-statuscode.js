#!/usr/bin/node
// script that display the status code of a GET request.
const url = process.argv[2];
const req = require('request');
req.get(url, function (err, res) {
  if (err) {
    console.error('code:', err);
  } else {
    console.log('code:', res.statusCode);
  }
});
