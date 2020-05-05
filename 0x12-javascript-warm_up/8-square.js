#!/usr/bin/node
// script that prints a square
const size = process.argv[2];
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
}
