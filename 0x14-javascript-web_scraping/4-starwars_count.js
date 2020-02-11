#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const json = JSON.parse(body);
  const wedgeUrl = 'https://swapi.co/api/people/18/';
  console.log(json.results.reduce((acc, result) => {
    return acc + (result.characters.some(el => el === wedgeUrl) ? 1 : 0);
  }, 0));
});
