#!/usr/bin/node
const reqeust = require('request');

reqeust(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  console.log('code: ' + res.statusCode);
});
