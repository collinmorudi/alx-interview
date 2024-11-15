#!/usr/bin/node

/*
  This script prints all characters of a Star Wars movie.

  Usage:
    node 0-starwars_characters.js <movie_id>

  Example:
    node 0-starwars_characters.js 3  # Prints characters from "Return of the Jedi"
*/

// eslint-disable-next-line import/no-extraneous-dependencies
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    // Create an array of promises for fetching character data
    const characterPromises = characterUrls.map((url) => new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    }));

    // Wait for all promises to resolve and then print character names
    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error(error);
      });
  } catch (error) {
    console.error(error);
  }
});

