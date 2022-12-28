#!/usr/bin/node
module.exports = class Rectangle {
  // module.exportsdeclaración está exportando una clase llamada Rectangle
  constructor (w, h) {
    this.width = w;
    this.height = h;
    // El constructor establece los valores de estos argumentos como propiedades de la Rectangleinstancia mediante la thispalabra clave
  }
};
