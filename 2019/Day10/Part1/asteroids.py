#!/usr/bin/python3

from var_dump import var_dump
import math
from collections import defaultdict


fh = open("input.txt", mode='r')
map_in = fh.read()
fh.close()

map_in = map_in.strip()
map_in = map_in.split("\n")

map_co = []

astr = []


for y in range(len(map_in)):
    for x in range(len(map_in[y])):
        if map_in[y][x] == "#":
            map_co.append({'y': y, 'x': x})


for i in range(len(map_co)):
    astr.append({})
    astr[i] = defaultdict(int)
    astr[i]['atan2'] = []

    for j in range(len(map_co)):
        dx = map_co[i]['y'] - map_co[j]['y']
        dy = map_co[i]['x'] - map_co[j]['x']

        astr[i]['y'] = map_co[i]['y']
        astr[i]['x'] = map_co[i]['x']
        astr[i]['atan2'].append(math.atan2(dy, dx))


for i in range(len(astr)):
    astr[i]['angles'] = defaultdict(int)
    
    for j in range(len(astr[i]['atan2'])):
        _r = astr[i]['atan2'][j]

        astr[i]['angles'][_r] = astr[i]['atan2'].count(_r)


for i in range(len(astr)):
    for j in astr[i]['angles']:
        astr[i]['visible'] += 1


best_v = 0
best_ms = ''
for i in range(len(astr)):
    print((astr[i]['x'], astr[i]['y']), astr[i]['visible'] )
    if astr[i]['visible'] > best_v:
        best_v = astr[i]['visible']
        best_ms = (astr[i]['x'], astr[i]['y'])

print("**", best_ms, best_v, "**")
