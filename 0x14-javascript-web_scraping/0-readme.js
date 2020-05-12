#!/usr/bin/node
// script that reads and prints the content of a file.
let aFile = process.argv[2];
const fs = require('fs');
fs.readFile(aFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    aFile = data;
    console.log(aFile);
  }
});
