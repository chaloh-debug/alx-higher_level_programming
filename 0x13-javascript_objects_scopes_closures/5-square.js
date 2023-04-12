#!/usr/bin/node
module.exports = class Square extends require('./rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
