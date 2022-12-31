#!/usr/bin/node
const square = require('./5-square');
/// herencia de square
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
    /// (super)función constructora con el parametro size pasado como el ancho y el alto del rectángulo.
    /// Esto crea un nuevo objeto con el mismo ancho y alto, creando efectivamente un cuadrado
  }

  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
            process.stdout.write(c);
        }
        console.log();
    }
  }
};
