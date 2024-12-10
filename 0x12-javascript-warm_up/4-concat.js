#!/usr/bin/node

const { argv } = require('node:process');

let arg2 = argv[2];
let arg3 = argv[3];

if (!argv[2]) {
  arg2 = 'undefined';
}
if (!argv[3]) {
  arg3 = 'undefined';
}

console.log(arg2, 'is', arg3);
