#!/usr/bin/node

exports.logMe = function (item) {
  this.counter = (this.counter === undefined) ? 0 : this.counter + 1;
  console.log(`${this.counter}: ${item}`);
};
