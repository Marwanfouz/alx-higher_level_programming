#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status Code: ${response.statusCode}`);
    process.exit(1);
  }

  const film = JSON.parse(body);

  if (!film || !film.characters || film.characters.length === 0) {
    console.error('No characters found for the specified movie ID.');
    process.exit(1);
  }

  const charactersUrls = film.characters;
  const charactersPromises = charactersUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject(error || `Status Code: ${response.statusCode}`);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error('Error fetching character:', error);
      process.exit(1);
    });
});
