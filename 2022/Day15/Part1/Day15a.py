#!/usr/bin/env python

import sys
import numpy as np
from icecream import ic
import re

def main () -> None:

    itxt = open("input", mode='r').readlines()
    itxt = [re.split('=|:|,', i.strip()) for i in itxt]
    mmap = [((int(i[1]),int(i[3])),(int(i[5]),int(i[7]))) for i in itxt]
    #itxt = [(np.array((int(i[1]),int(i[3]))),np.array((int(i[5]),int(i[7])))) for i in itxt]
    #sr = [(s[0], abs((s[0] - s[1])[0]) + abs((s[0] - s[1])[1])) for s in itxt]
    #xx = set()
    #xx = {((x, y),(-x, y),(x, -y),(-x, -y)) for s, r in sr for x in range(r+1) for y in range(0,(r+1)-x) }
    #ic(xx)
    #return
    
    sensors, beacons = [i[0] for i in mmap], [i[1] for i in mmap]
    
    ic(mmap)
    ic(sensors + beacons)
    smap = set()
    
    YTARGET = 10
    YTARGET = 2000000
    
    for sensor, beacon in mmap:
        rad = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        ic(sensor, rad)

        if sensor[1] < YTARGET:
            yreach = (np.array(sensor) + np.array((0, rad)))[1]
            if yreach < YTARGET: continue
        elif sensor[1] > YTARGET:
            yreach = (np.array(sensor) - np.array((0, rad)))[1]
            if yreach > YTARGET: continue
        else:
            pass

        for x in range(abs(yreach - YTARGET) + 1):
            if (sensor[0] + x, YTARGET) not in sensors + beacons:
                smap.add((sensor[0] + x, YTARGET))
            if (sensor[0] - x, YTARGET) not in sensors + beacons:
                smap.add((sensor[0] - x, YTARGET))
            
            #ic(sensor[0] + x, YTARGET)
            #ic(sensor[0] - x, YTARGET)

        if 0:
            for x in range(rad+1): 
                for y in range(0,(rad+1)-x):
                    #smap.update({tuple(np.array(sensor[0]) + coord) \
                    #    for coord in {(x, y),(-x, y),(x, -y),(-x, -y) }})
                    
                    for coord in {(x, y),(-x, y),(x, -y),(-x, -y)}:
                        if sensor[0][1] + coord[1] == YTARGET: 
                            ic((sensor[0][0] + coord[0], sensor[0][1] + coord[1]))
                            smap.add((sensor[0][0] + coord[0], sensor[0][1] + coord[1]))
    #ic(smap)

    ic()
    #x = [c for c in smap if c[1] == YTARGET and c not in [i[0] for i in mmap] and c not in [i[1] for i in mmap]]
    ic()
    #ic(len(x))
    ic(len(smap))


if __name__ == '__main__':
    sys.exit(main())
    