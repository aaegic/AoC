/*
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
*/

import { readFileSync } from 'fs';

const input: string[] = readFileSync('input.txt')
	.toString()
	.split('\n')

var GOODPASS:number = 0

input.forEach((l) => { 
	var _t0:string[] = l.split(' ')
	var _min: number = Number(_t0[0].split('-')[0])
	var _max: number = Number(_t0[0].split('-')[1])
	var _chr: string = _t0[1].split('')[0]
	var _str:string[] = _t0[2].split('')
	var __fc: number = 0
	
	_str.forEach(__c => { if (__c == _chr) { __fc++ } })

	if (__fc >= _min && __fc <= _max) { GOODPASS++ }
 })

console.log(GOODPASS)