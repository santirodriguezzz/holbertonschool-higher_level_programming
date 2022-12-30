#!/usr/bin/node
module.exports = class Rectangle {
  // module.exportsdeclaración está exportando una clase llamada Rectangle
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      // El constructor establece los valores de estos argumentos como propiedades de la Rectangle instancia mediante la thispalabra clave
    }
  }
};
