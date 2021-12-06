#!/usr/bin/env python

def draw(cords: list) -> list:
    if cords[0][0] != cords[1][0] and cords[0][1] != cords[1][1]:
        #diagonal
        dx = cords[0][0] - cords[1][0]
        dy = cords[0][1] - cords[1][1]

        for ds in range(1,abs(dx)):
            if dx < 0:
                nx = cords[0][0] + ds
            else:
                nx = cords[0][0] - ds
            
            if dy < 0:
                ny = cords[0][1] + ds
            else:
                ny = cords[0][1] - ds
            
            cords.append([nx,ny])
    else:
        #horizontal
        for c in range(cords[0][0]+1, cords[1][0]):
            cords.append([c, cords[0][1]])
        for c in range(cords[1][0]+1, cords[0][0]):
            cords.append([c, cords[0][1]])
                    
        #vertical
        for c in range(cords[0][1]+1, cords[1][1]):
            cords.append([cords[0][0], c])
        for c in range(cords[1][1]+1, cords[0][1]):
            cords.append([cords[0][0], c])
                    
    return cords


itxt = open("input", mode='r').read().strip().splitlines()

cords = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in itxt]

pnts = dict()

for cord in cords:
    for x, y in draw(cord):
        if (x, y) not in pnts:
            #python-esque multi-dimensional array using dict
            pnts.update({(x,y): 1})
        else:
            pnts.update({(x,y): 1 + pnts[(x,y)]})

n = [p for p in pnts if pnts[p] > 1]

print(len(n))

