#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  let myArray = [];
  for (let i = 2; i < argv.length; i++) {
    myArray[i - 2] = parseInt(argv[i]);
  }
  let biggest = Math.max.apply(null, myArray);
  i = myArray.indexOf(biggest);
  myArray[i] = 0;
  let secondBiggest = Math.max.apply(null, myArray);
  console.log(secondBiggest);
}
