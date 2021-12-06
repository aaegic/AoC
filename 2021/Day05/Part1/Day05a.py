#!/usr/bin/env python

def is_diag(cords: list) -> bool:
    if cords[0][0] != cords[1][0] and cords[0][1] != cords[1][1]: 
        return True
    else:
        return False


def draw(cords: list) -> list:
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

#filter out diagonals
cords = [cord for cord in cords if is_diag(cord) == False]

pnts = dict()

for cord in cords:
    for x, y in draw(cord):
        if (x, y) not in pnts:
            pnts.update({(x,y): 1})
        else:
            pnts.update({(x,y): 1 + pnts[(x,y)]})

n = [p for p in pnts if pnts[p] > 1]

print(len(n))