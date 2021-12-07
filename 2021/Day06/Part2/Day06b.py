#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()
itxt = list(map(int, itxt[0].split(',')))

fish = { 8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0, -1:0 }

for i in itxt:
    fish.update({i: fish.get(i) + 1})

for i in range(256):
    for k in range(0, 9):
        fish.update({ k-1: fish.get(k) })
    
    fish.update({ 8: fish.get(-1), 6: fish.get(6) + fish.get(-1), -1: 0 })
    
fish = sum([ v for k, v in fish.items()])

print(fish)
