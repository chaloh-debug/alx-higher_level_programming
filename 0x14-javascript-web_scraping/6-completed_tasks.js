#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error == null) {
    const dict = {};
    const data =JSON.parse(body);
    for (let i of data) {
        if (i.completed === true) {
            if (dict[i.userId] === undefined) {
              dict[i.userId] = 0;
            }
            dict[i.userId] +=1;
        }
    }
    console.log(dict);
  }
});
