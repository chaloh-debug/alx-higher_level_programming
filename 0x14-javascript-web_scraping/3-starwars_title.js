#!/usr/bin/node
const id = process.argv[2];
const url = ('https://swapi-api.alx-tools.com/api/films/' + id);
const request = require('request');

request(url, function(error, body, response) {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(body);
    console.log(data.title);
})
