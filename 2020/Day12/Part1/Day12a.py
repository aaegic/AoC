#!/usr/bin/python3

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

dl = intxt.strip().split("\n")

x, y, f = 0, 0, 0

dt = { 0: 'E', 90: 'S', 180: 'W', 270: 'N' }

def getdir(f, oa):
    f += oa
    
    if f > 270: 
        f -= 360
    elif f < 0:
        f += 360

    return f
    

for i in dl:
    oc = i[0]
    oa = int(i[1:])
    
    if oc == "R": f = getdir(f, oa)
    if oc == "L": f = getdir(f, oa * -1)
    
    if oc == "F": oc = dt.get(f)
    if oc == "N": y += oa
    if oc == "S": y -= oa
    if oc == "E": x += oa
    if oc == "W": x -= oa
    
print(x, y, abs(x) + abs(y))