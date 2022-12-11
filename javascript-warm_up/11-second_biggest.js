#!/usr/bin/node
const numbs = process.argv.slice(2);
if (numbs.length === 0) {
  console.log(0);
} else if (numbs.length === 1) {
  console.log(0);
} else {
  const sortnumbs = numbs.sort((a, b) => b - a);
  console.log(sortnumbs[1]);
}
