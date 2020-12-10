
//import * as fs from 'fs';
import { readFileSync } from 'fs';

let inputarr: number[] = readFileSync('input.txt')
	.toString()
	.split("\n")
	.map(Number);

inputarr.forEach(ei => {
	inputarr.forEach(ej => {
		inputarr.forEach(ek => {
			if (ei + ej + ek == 2020)
			{
				console.log({ ei, ej, ek })
				console.log(ei * ej * ek)
				process.exit(0)
			}
		});
	});
});
