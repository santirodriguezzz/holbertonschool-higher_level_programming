#!/usr/bin/node
const request = require('request');
const  path = process.argv[2];
request.readFile(path, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data);
    }
});