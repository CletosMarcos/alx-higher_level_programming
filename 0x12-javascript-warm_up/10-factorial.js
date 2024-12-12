#!/usr/bin/node

function factoria (value) {
  if (value === 0 || value === 1) {
    return 1;
  }
  return value * factoria(value - 1);
}

const factNr = parseInt(process.argv[2]);

if (factNr) {
  console.log(factoria(factNr));
} else {
  console.log(1);
}
