#!/usr/bin/node
exports.esrever = function (list) {
	let new = [];
	for (let i = list.length; i > 0; i--) {
		new.push(list[i]);
	}
	return new;
};
