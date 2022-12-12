#!/usr/bin/node
const request = require('request');
const url = require('url');
const filePath = process.argv[2];
request.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
