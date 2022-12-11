#!/usr/bin/node
const result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(result);
function add (a, b){
    return a + b;
};
