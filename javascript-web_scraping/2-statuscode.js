#!/usr/bin/node
const rq = require('request');
const args = process.argv[2];

rq(args, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
