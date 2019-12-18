#!/usr/bin/python3

from collections import defaultdict
from collections import Counter as counter
from operator import itemgetter
import numpy as np


fh = open("input.txt", mode='r')
map_in = fh.read()
fh.close()

map_in = map_in.strip()
map_in = map_in.split("\n")

map_co = []

astr = []


def rot90(_d):
    _d = _d - 90
    if _d < 0: _d = _d + 360
    return _d


for y in range(len(map_in)):
    for x in range(len(map_in[y])):
        if map_in[y][x] == "#":
            map_co.append({'y': y, 'x': x})


for i in range(len(map_co)):
    astr.append({})
    astr[i] = defaultdict(int)
    astr[i]['n'] = []
    astr[i]['y'] = map_co[i]['y']
    astr[i]['x'] = map_co[i]['x']
    astr[i]['v'] = 0

    for j in range(len(map_co)):
        dx = map_co[i]['y'] - map_co[j]['y']
        dy = map_co[i]['x'] - map_co[j]['x']

        astr[i]['n'].append({ 
            'y': map_co[j]['y'], 
            'x': map_co[j]['x'], 
            'a': rot90(np.degrees(np.arctan2(dx, dy)) % 360.0),
            #'a': np.degrees(np.arctan2(dx, dy)) % 360.0,
            'd': int(np.sqrt(dx**2 + dy**2) * 100),
            })


ms_i = 0
ms_v = 0

for i in range(len(astr)):
    astr[i]['n'].sort(key=lambda j: (j['a'], j['d']))
    
    for (j, k) in counter(map(itemgetter('a'), astr[i]['n'])).items():
        astr[i]['v'] += 1

    if astr[i]['v'] > ms_v:
        ms_v = astr[i]['v']
        ms_i = i

print(astr[ms_i]['v'])

e = 0
while e < 200:
    for j in range(len(astr[ms_i]['n'])):
        if astr[ms_i]['n'][j]['a'] == astr[ms_i]['n'][j-1]['a']:
            continue

        e = e + 1
        if e == 200:
            print(e,":", 
            astr[ms_i]['n'][j]['x'], 
            astr[ms_i]['n'][j]['y'], 
            (astr[ms_i]['n'][j]['x'] * 100) + astr[ms_i]['n'][j]['y']
            )
