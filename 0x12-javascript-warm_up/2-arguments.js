#!/usr/bin/node
let msg;
if (process.argv.length < 3) {
  msg = 'No argument';
} else if (process.argv.length === 3) {
  msg = 'Argument found';
} else {
  msg = 'Arguments found';
}
console.log(msg);
