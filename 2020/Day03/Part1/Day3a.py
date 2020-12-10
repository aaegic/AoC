#!/usr/bin/python3

from var_dump import var_dump
import math
from collections import defaultdict


fh = open("input.txt", mode='r')
map_in = fh.read()
fh.close()

map_in = map_in.strip()
map_in = map_in.split("\n")

map_ff = []
trees = 0

for row in map_in:
	map_ff.append(list(row))


for row in range(1, len(map_ff)):
    col = row * 3
    if col > len(map_ff[0]):
        sub = math.floor(col / len(map_ff[0]))
        col = col - sub * len(map_ff[0])
        
    if map_ff[row][col] == "#":
        trees += 1
        print(row, col, map_ff[row][col])


print(trees)
