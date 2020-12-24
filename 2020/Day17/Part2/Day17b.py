#!/usr/bin/python3

import copy

fh = open("input.txt")
intxt = fh.read()
fh.close()

cubes1 = set()
cubes2 = set()

def countnc (cube: set, cubes: set) -> set:
    retn = set()
    for x in (-1, 0, +1):
        for y in (-1, 0, +1):
            for z in (-1, 0, +1):
                for w in (-1, 0, +1):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    elif (cube[0]  + x, cube[1] + y, cube[2] + z, cube[3] + w)  in cubes:
                        retn.add((cube[0]  + x, cube[1] + y, cube[2] + z, cube[3] + w))
    
    return retn

def shownp (cube: set, cubes: set) -> set:
    retn = set()
    for x in (-1, 0, +1):
        for y in (-1, 0, +1):
            for z in (-1, 0, +1):
                for w in (-1, 0, +1):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    else:
                        retn.add((cube[0]  + x, cube[1] + y, cube[2] + z, cube[3] + w))
    
    return retn

for y, row in enumerate(list(intxt.split('\n'))):
    for x, e in enumerate(list(row)):
        if e == '#':
            cubes1.add((x, y, 0, 0))

for _ in range(6):
    for cube in cubes1:
        if 2 <= len(countnc(cube, cubes1)) <= 3:
            cubes2.add(cube)

        for cubep in shownp(cube, cubes1):
            if len(countnc(cubep, cubes1)) == 3 and not cubep in cubes1:
                cubes2.add(cubep)
                
    cubes1 = copy.deepcopy(cubes2)
    cubes2.clear()

for n in cubes1:
    print(n)
    