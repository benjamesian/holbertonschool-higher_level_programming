#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];
  for (const el of list) {
    out.unshift(el);
  }
  return out;
};
