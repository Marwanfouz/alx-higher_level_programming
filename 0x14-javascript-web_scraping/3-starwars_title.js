#!/usr/bin/node
const reqeust = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
reqeust(api, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
