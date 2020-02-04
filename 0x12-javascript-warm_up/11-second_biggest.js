#!/usr/bin/node
let args = process.argv;
args.shift();
args.shift();
args = args.map(el => parseInt(el));
args.sort((a, b) => a - b);
args.pop();
console.log(args.pop() || 0);
