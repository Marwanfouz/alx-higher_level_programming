#!/usr/bin/node
const number = Number(process.argv[2]);
if (isNaN(number)) {
    console.log('Missing size');
} else {
    let mySquare;
    for (let i = 0; i < number; i++) {
        mySquare = '';
        for (let j = 0; j < number; j++) {
            mySquare += 'X';
        }
        console.log(mySquare);
    }
}
