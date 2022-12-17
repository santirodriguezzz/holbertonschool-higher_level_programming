#!/usr/bin/node
const request = require('request');
const rq = require('fs');
const args = process.argv;
let web = 'a';

request(args[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  web = body;
  fs.writeFile(args[3], web, 'utf-8', (error) => {
    if (error) {
      throw error;
    }
  });
});
