#!/usr/bin/node
const reqeust = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
reqeust(url, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(err);
    return;
  }
  fs.writeFile(filename, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
