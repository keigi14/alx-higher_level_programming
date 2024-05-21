#!/usr/bin/node
const request = require('request');

const _episodeId = process.argv[2];

if (parseInt(_episodeId) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + _episodeId;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
