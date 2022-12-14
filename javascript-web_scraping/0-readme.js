#!/usr/bin/node
const request = require('request');
const path = process.argv;

request.readFile(path[2], 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
