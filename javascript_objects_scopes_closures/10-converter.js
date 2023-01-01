#!/usr/bin/node
exports.converter = function (base) {
  function conversor (item) {
    return item.toString(base);
  }
  return conversor;
};
