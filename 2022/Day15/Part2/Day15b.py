#!/usr/bin/env python

import sys
import numpy as np
from icecream import ic
import re

def main () -> None:

    itxt = open("input-test", mode='r').readlines()
    itxt = [re.split('=|:|,', i.strip()) for i in itxt]
    itxt = [((int(i[1]),int(i[3])),(int(i[5]),int(i[7]))) for i in itxt]

    sensors, beacons = [i[0] for i in itxt], [i[1] for i in itxt]

    RANGE = 20
    #RANGE = 4000000
    
    smap = set()
    mrow = set()
    
    for y in [10]:#range(RANGE + 1):
        mrow = {(i[0], i[0]) for i in sensors + beacons if i[1] == y}
        ic(y)
        for sensor, beacon in zip(sensors, beacons):
            rad = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

            if sensor[1] < y:
                yreach = (np.array(sensor) + np.array((0, rad)))[1]
                if yreach < y: continue
                xreach = yreach - y
            elif sensor[1] > y:
                yreach = (np.array(sensor) - np.array((0, rad)))[1]
                if yreach > y: continue
                xreach = yreach - y
            else:
                xreach = rad

            mrow.add(tuple(sorted((-(sensor[0] + xreach), sensor[0] + xreach))))

            if 0:
                for x in range(abs(xreach) + 1):
                    if sensor[0] + x not in mrow:
                        #if 0 < sensor[0] + x <= RANGE:
                        mrow.add(sensor[0] + x)
                        ic(sensor[0] + x)
                    if sensor[0] - x not in mrow:
                        #if 0 < sensor[0] - x <= RANGE:
                        mrow.add(sensor[0] - x)
                        ic(sensor[0] - x)
        
        ic(y, mrow)
        
        mrow = sorted(mrow)
        ic(mrow)
        
        frow = [list(mrow[0])]
        ic(frow)
        
        for i in range(1,len(mrow)):
            if frow[-1][1] <= mrow[i][1]:
                ic()
                frow[-1][1] = mrow[i][1]
            elif mrow[i] not in frow:
                ic()
                frow.append(list(mrow[i]))
            
        ic(frow)
                
            
            
            
        
        
        
        
        
        #for x in range(RANGE + 1):
        #    if x not in mrow:
        #        ic((x,y))
        #        smap.add((x, y))
            
    ic(smap)
    ic(len(smap))


if __name__ == '__main__':
    sys.exit(main())
    