#!/usr/bin/node
// "34e" is not a number
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : num);
