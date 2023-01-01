#!/usr/bin/node
module.exports.esrever = function (list) {
  const i = [];
  for (let iter = list.length - 1; iter >= 0; iter--) {
    i.push(list[iter]);
  }
  return i;
};
