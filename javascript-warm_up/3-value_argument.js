#!/usr/bin/node

const argument = process.argv[2];

if (argument === undefined) {
	console.log('No Argument');
}	else {
	console.log(argument);
}
