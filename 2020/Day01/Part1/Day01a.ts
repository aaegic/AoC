
//import * as fs from 'fs';
import { readFileSync } from 'fs';
import { exit } from 'process';

let inputtxt:string = readFileSync('input.txt').toString();
let inputarr:number[] = inputtxt.split("\n").map(Number);

inputarr.forEach(ei => {
	inputarr.forEach(ej => {
		if (ei + ej == 2020) {
			console.log(ei)
			console.log(ej)
			console.log(ei * ej);
			process.exit(0);
		}
	});
});
