#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const argv = process.argv;
const size = argv.length;
let i;
let myArray = [];
let biggest;
let secondBiggest;
if (size <= 3) {
  console.log(0);
} else {
  for (i = 2; i < size; i++) {
    myArray[i - 2] = parseInt(argv[i]);
  }
  biggest = Math.max.apply(null, myArray);
  myArray.splice(myArray.indexOf(biggest), 1);
  secondBiggest = Math.max.apply(null, myArray);
  console.log(secondBiggest);
}
