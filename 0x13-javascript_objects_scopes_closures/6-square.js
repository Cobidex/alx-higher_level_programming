#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let myChar = 'X';
    if (c) {
      myChar = 'C';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(myChar.repeat(this.width));
    }
  }
}

module.exports = Square;
