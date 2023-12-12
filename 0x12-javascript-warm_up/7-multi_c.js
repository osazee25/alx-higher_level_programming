#!/usr/bin/node

const n_occur = parseInt(process.argv[2]);

if (!isNaN(n_occur)) {
	for (let i = 0; i < n_occur; i++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
