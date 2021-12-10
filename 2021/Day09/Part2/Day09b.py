#!/usr/bin/env python

import sys

def main () -> int:
    itxt = open("input", mode='r').read().strip().splitlines()

    lava = {(i,j): int(v) for i, r in enumerate(itxt) for j, v in enumerate(r)}
    last = {'r': max([r for (r,c) in lava.keys()]), 'c': max([c for (r,c) in lava.keys()])}
    lwps = list()
    bsns = list()
    
    def getns(r: int, c:int) -> set:
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last['r'] and i[1] >= 0 and i[1] <= last['c']]


    def getbs(r: int, c:int, hist: set) -> set:
        ns = getns(r, c)
        
        hist.add((r, c))
        
        for i in ns:
            if lava.get(i) < 9:
                base.add(i)
        
        for r, c in ns:
            if (r, c) not in hist and lava.get((r,c)) < 9:
                getbs(r, c, hist)


    for r in range(last['r']+1):
        for c in range(last['c']+1):
            ncrds = getns(r, c)

            nval = [lava.get(i) for i in ncrds]

            if lava.get((r,c)) < min(nval):
                lwps.append((r,c))

    for r, c in lwps:
        hist = set()
        base = set()

        getbs(r,c, hist)

        bsns.append(base)

    
    bsns.sort(key=len)
    print(len(bsns[-1]) * len(bsns[-2]) * len(bsns[-3]))
    
    return 0


if __name__ == '__main__':
    sys.exit(main()) 