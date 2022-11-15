#!/usr/bin/node
// script to read a file and output the content
let fs = require('fs');
let process = require('process');
let args = process.argv;
fs.readFile(args[2], 'utf8', function(err, data){
	if (err) throw err;
	console.log(data);
});
