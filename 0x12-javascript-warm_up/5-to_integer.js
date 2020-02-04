#!/usr/bin/node
// "34e" is not a number
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
    console.log('Not a number')
} else {
    console.log(`My number: ${num}`)
}
