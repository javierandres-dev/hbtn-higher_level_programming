#!/usr/bin/node
//  script that writes a string to a file.
let fPath = process.argv[2];
let toWrite = process.argv[3];
const fs = require('fs');
fs.writeFile(fPath, toWrite, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
