#!/usr/bin/env python

import sys
import numpy as np
from icecream import ic
import re

def main () -> None:

    itxt = open("input-test", mode='r').readlines()
    itxt = [re.split('=|:|,', i.strip()) for i in itxt]
    itxt = [((int(i[1]),int(i[3])),(int(i[5]),int(i[7]))) for i in itxt]
    #itxt = [(np.array((int(i[1]),int(i[3]))),np.array((int(i[5]),int(i[7])))) for i in itxt]
    #sr = [(s[0], abs((s[0] - s[1])[0]) + abs((s[0] - s[1])[1])) for s in itxt]
    #xx = set()
    #xx = {((x, y),(-x, y),(x, -y),(-x, -y)) for s, r in sr for x in range(r+1) for y in range(0,(r+1)-x) }
    #ic(xx)
    #return
    
    #ss, bs = [i[0] for i in itxt], [i[1] for i in itxt]
    
    
    smap = set()
    
    for sensor in itxt:
        d = np.array(sensor[0]) - np.array(sensor[1])
        r = abs(d[0]) + abs(d[1])

        for x in range(r+1): 
            for y in range(0,(r+1)-x):
                smap.update({tuple(np.array(sensor[0]) + coord) \
                    for coord in {(x, y),(-x, y),(x, -y),(-x, -y)}})
                
                #for c in {(x, y),(-x, y),(x, -y),(-x, -y)}:
                #    smap.add(tuple(np.array(s[0]) + c))
            
    #ic(smap)

    x = [c for c in smap if c[1] == 10 and c not in [i[0] for i in itxt] and c not in [i[1] for i in itxt]]
    ic(x, len(x))


if __name__ == '__main__':
    sys.exit(main())
    