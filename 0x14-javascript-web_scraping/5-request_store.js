#!/usr/bin/node
const url = process.argv[2];
const file_name = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error == null) {
    fs.writeFileSync(file_name, body);
  }
});
