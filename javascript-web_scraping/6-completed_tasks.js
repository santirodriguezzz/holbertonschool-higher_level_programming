#!/usr/bin/node

const request = require('request');
const arg = process.argv;
let info = '';
const mapi = {};

request(arg[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  info = JSON.parse(body);

  for (let index = 0; index < info.length; index++) {
    const useMe = info[index].userId;

    if (info[index].completed) {
      mapi[useMe] = 0;

      for (let index2 = 0; index2 < info.length; index2++) {
        if (info[index].userId === info[index2].userId) {
          if (info[index2].completed === true) {
            mapi[useMe] = mapi[useMe] + 1;
          }
        }
      }
    }
  }

  console.log(mapi);
});
