#!/usr/bin/node
const reques = require('reques');
const path = process.argv;

reques.readFile(path[2], 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});