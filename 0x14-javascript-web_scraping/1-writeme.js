#!/usr/bin/node
const fs = require('fs');
const _file = process.argv[2];
const content = process.argv[3];
fs.writeFile(_file, content, 'utf-8', function (err) {
		if (err) {
		console.log(err);
		}
		});
