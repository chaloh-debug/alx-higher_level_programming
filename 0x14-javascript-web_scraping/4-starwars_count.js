#!/usr/bin/node
const url = process.argv[2];
const id = 18;
let count = 0;
const request = require('request');

request(url, function(error, response, body) {
  if (error == null) {
    const data = JSON.parse(body);
      for (const res of data.results) {
          for (const char of res.characters) {
              if (char.search(id) > 0) {
                  count++;
              }
          }
      }
      console.log(count);
  }
});
