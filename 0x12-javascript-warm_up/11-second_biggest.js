#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const argv = process.argv;
const size = argv.length;
function mySol (argv) {
  if (size > 3) {
    let result = argv.sort();
    result = argv.slice(size - 2, - 1);
    return result[0];
  } else {
    return 0;
  }
}
console.log(mySol(argv));
