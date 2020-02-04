#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let row = '';
  let i = 0;
  for (i = 0; i < num; i++) {
    row += 'X';
  }
  for (i = 0; i < num; i++) {
    console.log(row);
  }
}
