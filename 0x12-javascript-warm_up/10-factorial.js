#!/usr/bin/node

function factorial (value) {
  let accumulator = 1;
  value = parseInt(value);

  if (!value) {
    return 1;
  }
  while (value > 0) {
    accumulator *= value;
    value--;
  }
  return accumulator;
}

const factNr = process.argv[2];
console.log(factorial(factNr));
