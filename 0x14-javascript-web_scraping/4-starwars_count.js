#!/usr/bin/node
const reqeust = require('request');
const api = process.argv[2];
reqeust(api, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(err);
    return;
  }
  const count = body.split('/people/18/').length - 1;
  console.log(count);
});
