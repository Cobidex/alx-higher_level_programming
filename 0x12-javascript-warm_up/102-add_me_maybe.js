#!/usr/bin/node
exports.incrementAndCall = function (number, theFunction) {
  theFunction(number + 1);
};
