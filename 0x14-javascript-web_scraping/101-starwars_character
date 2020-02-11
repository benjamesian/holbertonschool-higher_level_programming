#!/usr/bin/node
const request = require('request');

request.get(`http://swapi.co/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const json = JSON.parse(body);
  (function printNextCharacter (urls) {
    request.get(urls.shift(), (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const json = JSON.parse(body);
      console.log(json.name);
      if (urls.length > 0) {
        printNextCharacter(urls);
      }
    });
  })(json.characters);
});
