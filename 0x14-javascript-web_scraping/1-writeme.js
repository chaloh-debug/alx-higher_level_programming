#!/usr/bin/node
const fs = require('fs');
const fname = process.argv[2];
const content = process.argv[3];
fs.writeFile(fname, content, (err) => {
  if (err) throw err;
});
