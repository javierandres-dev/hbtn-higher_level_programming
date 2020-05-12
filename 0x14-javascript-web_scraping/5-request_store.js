#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const process = require('process');
const fs = require('fs');
const urlReq = process.argv[2];
const pathRes = process.argv[3];
request(urlReq, function (err, res, data){
  if (err == null) {
    fs.writeFile(pathRes, data, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
