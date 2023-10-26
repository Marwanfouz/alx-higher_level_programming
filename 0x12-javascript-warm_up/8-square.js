#!/usr/bin/node
const len = Number(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing size');
} else {
  let mySqure;
  for (let i = 0; i < len; i++) {
    mySqure = '';
    for (let j = 0; j < len; j++) {
      mySqure += 'X';
    }
    console.log(mySqure);
  }
}
