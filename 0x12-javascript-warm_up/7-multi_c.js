#!/usr/bin/node
// script that prints x times “C is fun”
const xTimes = process.argv[2];
let text = 'C is fun';
if (xTimes === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < xTimes; i++) {
    console.log(text);
  }
}
