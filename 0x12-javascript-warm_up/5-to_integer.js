#!/usr/bin/node
// "34e" is not a number
const num = parseInt(process.argv[2]);
console.log(isNaN(num) ? 'Not a number' : num);
