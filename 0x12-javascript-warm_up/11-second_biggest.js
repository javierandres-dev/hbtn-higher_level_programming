#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const argv = process.argv;
const size = argv.length;
function mySol (argv) {
  if (size <= 3) {
    return 0;
} else {
    let myArray = [];
    for (let i = 2; i < size; i++) {
      myArray[i - 2] = parseInt(argv[i]);
    }
    let biggest = Math.max.apply(null, myArray);
    myArray.splice(myArray.indexOf(biggest), 1);
    let secondBiggest = Math.max.apply(null, myArray);
    return secondBiggest;
  }
}
console.log(mySol(argv));
