#!/usr/bin/node
const square = require('./5-square');
/// herencia de square
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
    /// (super)función constructora con el parametro size pasado como el ancho y el alto del rectángulo.
    /// Esto crea un nuevo objeto con el mismo ancho y alto, creando efectivamente un cuadrado
  }

  charPrint (c = 'X') {
    this.print(c);
  }
};
