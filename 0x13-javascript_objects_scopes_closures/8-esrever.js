#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  let x = 0;
  while ((length - x) > 0) {
    const aux = list[length];
    list[length] = list[x];
    list[x] = aux;
    x++;
    length--;
  }
  return list;
};
