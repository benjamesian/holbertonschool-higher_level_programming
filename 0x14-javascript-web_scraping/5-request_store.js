#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(process.argv[3], body, err => console.log(err));
});
