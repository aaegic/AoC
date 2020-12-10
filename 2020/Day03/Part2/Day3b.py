#!/usr/bin/python3

slo = [
    { 'x': 1, 'y': 1 },
    { 'x': 3, 'y': 1 },
    { 'x': 5, 'y': 1 },
    { 'x': 7, 'y': 1 },
    { 'x': 1, 'y': 2 }
]

from var_dump import var_dump
import math
from collections import defaultdict

fh = open("input.txt", mode='r')
map_in = fh.read()
fh.close()

map_in = map_in.strip()
map_in = map_in.split("\n")

map_ff = []
trees = []

for row in map_in:
	map_ff.append(list(row))

for _slo in slo:
    _t = 0
    row = _slo['y']
    col = _slo['x']

    while row < len(map_ff):
        if col > len(map_ff[0]) - 1:
            sub = math.floor(col / len(map_ff[0]))
            col = col - (sub * len(map_ff[0]))
        
        if map_ff[row][col] == "#":
            _t += 1

        row += _slo['y']
        col += _slo['x']

    trees.append(_t)

print(math.prod(trees))