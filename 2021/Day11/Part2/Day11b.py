#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()

octopi = {(i,j): int(v) for i, r in enumerate(itxt) for j, v in enumerate(r)}
last = {'r': max([r for (r,c) in octopi.keys()]), 'c': max([c for (r,c) in octopi.keys()])}

it = 0

def getns(r: int, c:int) -> set:
    return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r+1,c-1),(r-1,c+1)] \
        if i[0] >= 0 and i[0] <= last['r'] and i[1] >= 0 and i[1] <= last['c']]

while len(set(octopi.values())) > 1:
    flashed = set()
    
    #increment all
    octopi = {i: int(v+1) for i, v in octopi.items()}
    
    while len(flash := {(r,c) for ((r,c),v) in octopi.items() \
            if (r,c) not in flashed and v >= 10}) > 0:

        flashed.update(flash)
        
        flashns = [getns(r,c) for (r,c) in flash]

        for i in flashns:
            for (r,c) in i:
                octopi.update({(r,c): octopi.get((r,c))+1})
        
    for ((r,c),v) in octopi.items():
        if v > 9:
            octopi.update({(r,c):0})
            
    it += 1

print(it)
