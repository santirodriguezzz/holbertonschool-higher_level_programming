#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/// herencia de rectangle
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    /// (super)función constructora con el parametro size pasado como el ancho y el alto del rectángulo.
    /// Esto crea un nuevo objeto con el mismo ancho y alto, creando efectivamente un cuadrado
  }
};
