#!/usr/bin/node

const argList = process.argv;

if (argList.length < 4) {
  console.log(0);
} else {
  const secondBiggest = argList.length - 2;

  for (let i = 2; i < argList.length - 1; i++) {
    for (let j = 2; j < argList.length - 1; j++) {
      let aux;
      if (parseInt(argList[j]) > parseInt(argList[j + 1])) {
        aux = argList[j];
        argList[j] = argList[j + 1];
        argList[j + 1] = aux;
      }
    }
  }
  console.log(argList[secondBiggest]);
}
