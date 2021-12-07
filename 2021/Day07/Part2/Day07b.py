#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()
crab = list(map(int, itxt[0].split(',')))

fuel = min([sum([sum(range(1,abs(i-c)+1)) for c in crab]) for i in range(max(crab)*2)])

print(fuel)

