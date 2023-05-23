#!/usr/bin/node
const fs = require('fs');
const file_name = process.argv[2];
let content = process.argv[3];
fs.writeFile(file_name, content, (err) => {
    if (err) throw err;
});
