#!/usr/bin/python3

import math

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

dl = intxt.strip().split("\n")

sx, sy = 0, 0
wx, wy = 10, 1

for i in dl:
    oc = i[0]
    oa = int(i[1:])
    
    if oc == "R" or oc == "L":
        if oc == "R": ar = math.radians(oa * -1)
        elif oc == "L": ar = math.radians(oa)
        
        dx = round(math.cos(ar) * wx - math.sin(ar) * wy)
        dy = round(math.sin(ar) * wx + math.cos(ar) * wy)
        wx, wy = dx, dy
    
    elif oc == "N": wy += oa
    elif oc == "S": wy -= oa
    elif oc == "E": wx += oa
    elif oc == "W": wx -= oa
    elif oc == "F":
        sx += wx * oa
        sy += wy * oa

    print(wx, wy, sx, sy)
    
print(abs(sx) + abs(sy))