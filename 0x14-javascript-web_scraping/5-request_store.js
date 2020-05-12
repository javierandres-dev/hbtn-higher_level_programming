#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const urlReq = process.argv[2];
const pathRes = process.argv[3];
const req = require('request');
const fs = require('fs');
req(urlReq, 'UTF-8', function (err, res, data){
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(pathRes, data);
  }
});
