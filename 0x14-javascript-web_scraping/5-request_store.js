#!/usr/bin/node
const url = process.argv[2];
const fname = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error == null) {
    fs.writeFileSync(fname, body);
  }
});
