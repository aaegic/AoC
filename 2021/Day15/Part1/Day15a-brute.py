#!/usr/bin/env python

from functools import lru_cache
from var_dump import var_dump
import sys

def main () -> int:

    itxt = open("input", mode='r').read().strip().splitlines()

    rmap = {(i,j): int(v) for i, r in enumerate(itxt) for j, v in enumerate(r)}
    last = (max([r for (r,c) in rmap.keys()]), max([c for (r,c) in rmap.keys()]))

    paths = list()
    risk = int()

    def getns(r: int, c: int) -> set:
        #return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r+1,c-1),(r-1,c+1)] \
        #    if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]
        return [i for i in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]

    def getvs(np) -> set:
        nd = {ik: iv for ik, iv in rmap.items() if ik in getns(*np)}
        nd = dict(sorted(nd.items(), key=lambda i: i[1])) 
        nd = list(nd)
        return(nd)

    @lru_cache(maxsize = 1000)
    def walk(pos: str, path: tuple) -> list:
        nonlocal risk
        if pos in path:
            return

        path = path +(pos,)
        
        if risk:
            if sum([rmap.get(j) for j in path]) > risk:
                return
        
        if last in path:
            #paths.append(path)
            risk = sum([rmap.get(j) for j in path])
            print(risk)
            return path
        
        for p in getvs(pos):
            #recursion
            #pass by reference pass by value make a list() or you'll be sorry
            walk(p, tuple(path))

    pos = (0,0)

    walk(pos, ())

    #risk = [sum([rmap.get(j) for j in i]) for i in paths]

    print(risk - rmap.get((0,0)))

if __name__ == '__main__':
    sys.exit(main()) 