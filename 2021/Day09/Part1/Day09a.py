#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()

lava = {(i,j): int(v) for i, r in enumerate(itxt) for j, v in enumerate(r)}
last = {'r': max([r for (r,c) in lava.keys()]), 'c': max([c for (r,c) in lava.keys()])}
risk = list()

for r in range(last['r']+1):
    for c in range(last['c']+1):
        ncrd = [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last['r'] and i[1] >= 0 and i[1] <= last['c']]
        
        nval = [lava.get(i) for i in ncrd]

        if lava.get((r,c)) < min(nval):
            risk.append(lava.get((r,c))+1)

print(sum(risk))
