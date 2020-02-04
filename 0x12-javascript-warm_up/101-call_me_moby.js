#!/usr/bin/node
exports.callMeMody = function (x, theFunction) {
  while (x--) { theFunction(); }
};
