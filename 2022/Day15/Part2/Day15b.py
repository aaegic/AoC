#!/usr/bin/env python

import sys
import numpy as np
from numpy.linalg import norm 
import matplotlib.pyplot as plt
import math 
from icecream import ic
import re

def main () -> None:

    #https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
    
    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

    print line_intersection((A, B), (C, D))
    
    
    itxt = open("input-test", mode='r').readlines()
    itxt = [re.split('=|:|,', i.strip()) for i in itxt]
    itxt = [((int(i[1]),int(i[3])),(int(i[5]),int(i[7]))) for i in itxt]

    sensors, beacons = [i[0] for i in itxt], [i[1] for i in itxt]

    smap = set()
    edges_p = set()
    edges_n = set()
    
    for sensor, beacon in zip(sensors, beacons):
        rad = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        rad = norm(np.array(np.array(sensor) - np.array(beacon)), 1)
        
        ic(rad)
        xs = []
        ys = []

        edges_p.update({
            ((sensor[0] + rad, sensor[1]),(sensor[0], sensor[1] + rad)),    # / bottom right
            ((sensor[0] - rad, sensor[1]),(sensor[0], sensor[1] - rad)) })  # / top left
        
        xs.append(sensor[0] + rad)
        ys.append(sensor[1])
        xs.append(sensor[0])
        ys.append(sensor[1] + rad)
        
        plt.plot(xs, ys, linestyle = 'dotted')
        xs = []
        ys = []
        
        xs.append(sensor[0] - rad)
        ys.append(sensor[1])
        xs.append(sensor[0])
        ys.append(sensor[1] - rad)
        
        plt.plot(xs, ys, linestyle = 'dotted')
        
        
        edges_n.update({
            ((sensor[0], sensor[1] + rad),(sensor[0] - rad, sensor[1])),    # \ bottom left
            ((sensor[0], sensor[1] - rad),(sensor[0] + rad, sensor[1])) })  # \ top right

        xs = []
        ys = []

        xs.append(sensor[0])
        ys.append(sensor[1] + rad)
        xs.append(sensor[0] - rad)
        ys.append(sensor[1])
        
        plt.plot(xs, ys, linestyle = 'dotted')
        xs = []
        ys = []
        
        xs.append(sensor[0])
        ys.append(sensor[1] - rad)
        xs.append(sensor[0] + rad)
        ys.append(sensor[1])

        plt.plot(xs, ys, linestyle = 'dotted')


    ic(edges_n)
    ic(edges_p)
    plt.show()
    
















    return


            
    ic(smap)
    ic(len(smap))


if __name__ == '__main__':
    sys.exit(main())
    