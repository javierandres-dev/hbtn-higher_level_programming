#!/usr/bin/node
// script that prints x times “C is fun”
const x = process.argv[2];
let text = 'C is fun';
if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(text);
  }
}
