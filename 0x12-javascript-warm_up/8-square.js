#!/usr/bin/node

const size = process.argv[2];

if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    let chars = '';

    for (let j = 0; j < size; j++) {
      chars += 'X';
    }
    console.log(chars);
  }
} else {
  console.log('Missing size');
}
