#!/usr/bin/node
const fname = process.argv[2];
const fs = require('fs');
fs.readFile(fname, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString('utf8'));
});
