#!/usr/bin/node
const file_name = process.argv[2];
const fs = require('fs');
fs.readFile(file_name, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString('utf8'));
});
