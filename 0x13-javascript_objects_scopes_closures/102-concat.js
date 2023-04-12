#!/usr/bin/node
const argv = require('process');
const fs = require('fs');

const arg1 = fs.readFileSync(argv[2]);
const arg2 = fs.readFileSync(argv[3]);
fs.writeFileSync(argv[4], arg1 + arg2);
