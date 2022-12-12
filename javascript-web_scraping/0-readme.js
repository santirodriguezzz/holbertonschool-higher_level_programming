#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
request.readFile(path, 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  } else {
    console.log(data);
  }
});
