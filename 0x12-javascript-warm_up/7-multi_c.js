#!/usr/bin/node

const nrOccurrences = parseInt(process.argv[2]);

if (!nrOccurrences) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nrOccurrences; i++) {
    console.log('C is fun');
  }
}
