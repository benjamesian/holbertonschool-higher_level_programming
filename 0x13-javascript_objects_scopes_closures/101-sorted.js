#!/usr/bin/node

const dict = require('./101-data').dict;

const d = {};
for (const el in dict) {
  d[dict[el]] = d[dict[el]] || [];
  d[dict[el]].push(el);
}

console.log(d);
