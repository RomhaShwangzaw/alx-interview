#!/usr/bin/node
// Prints all characters of a Star Wars movie

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <id>');
  process.exit(1);
}

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, __, body) => {
  // Printing error if it occurs
  if (error) console.error(error);
  const charactersURL = JSON.parse(body).characters;
  displayCharacters(charactersURL);
});

function displayCharacters (charactersURL) {
  const charactersName = charactersURL.map(
    url => new Promise((resolve, reject) => {
      request(url, (error, __, body) => {
        if (error) reject(error);
        resolve(JSON.parse(body).name);
      });
    }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(error => console.log(error));
}
