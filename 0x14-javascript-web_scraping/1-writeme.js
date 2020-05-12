#!/usr/bin/node
//  script that writes a string to a file.
let fPath = process.argv[2];
let content = process.argv[3];
const fs = require('fs');
fs.writeFile(fPath, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
