#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body).characters;
  for (const characters of data) {
    request(characters, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(err);
        return;
      }
      const movie = JSON.parse(body);
      console.log(movie.name);
    });
  }
});
