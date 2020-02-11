#!/usr/bin/node
const request = require('request');

request.get(`http://swapi.co/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const json = JSON.parse(body);
  json.characters.forEach(url => request.get(url, (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const character = JSON.parse(body);
    console.log(character.name);
  }));
});
