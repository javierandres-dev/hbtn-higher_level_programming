#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const process = require('process');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error == null) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
