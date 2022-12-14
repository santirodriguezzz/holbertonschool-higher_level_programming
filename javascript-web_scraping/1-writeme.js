#!/usr/bin/node
const rq = require('fs');
const args = process.argv;
const data = args[3];

rq.writeFile(args[2], data, 'utf8', (err) => {
  if (err) {
    return console.log(err);
  }
});
