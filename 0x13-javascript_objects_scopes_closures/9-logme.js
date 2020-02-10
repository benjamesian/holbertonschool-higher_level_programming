#!/usr/bin/node

exports.logMe = function (item) {
  logMe.counter = (logMe.counter || -1) + 1;
  console.log(`${logMe.counter}: ${item}`); 
};
