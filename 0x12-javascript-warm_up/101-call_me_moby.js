#!/usr/bin/node
exports.callMeMody = function (x, theFunction) {
  while (x-- > 0) { theFunction(); }
};
