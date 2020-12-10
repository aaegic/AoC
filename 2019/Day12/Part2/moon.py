#!/usr/bin/python3

from var_dump import var_dump
from collections import defaultdict
import numpy as np


"""https://twitter.com/Dementophobia/status/1205239170219814934"""

""" Example 3
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""
""" Example 1
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""
""" Input
<x=-8, y=-9, z=-7>
<x=-5, y=2, z=-1>
<x=11, y=8, z=-14>
<x=1, y=-4, z=-11>
"""

moon = []
moon.append([])
moon[0] = []
moon[0].append(defaultdict(int, {
    'name': "Io",
    'px': -8, 'py': -9, 'pz': -7,
    'vx': 0, 'vy': 0, 'vz': 0
    }))
moon.append([])
moon[1] = []
moon[1].append(defaultdict(int, {
    'name': "Europa",
    'px': -5, 'py': 2, 'pz': -1,
    'vx': 0, 'vy': 0, 'vz': 0
    }))
moon.append([])
moon[2] = []
moon[2].append(defaultdict(int, {
    'name': "Ganymede",
    'px': 11, 'py': 8, 'pz': -14,
    'vx': 0, 'vy': 0, 'vz': 0
    }))
moon.append([])
moon[3] = []
moon[3].append(defaultdict(int, {
    'name': "Callisto",
    'px': 1, 'py': -4, 'pz': -11,
    'vx': 0, 'vy': 0, 'vz': 0
    }))

bang = moon

iterations = 1000

for step in range(iterations):
    for m1 in range(len(moon)):
        moon[m1].append(defaultdict(int))

        moon[m1][-1]['name'] = moon[m1][step]['name']
        moon[m1][-1]['vx'] = moon[m1][step]['vx']
        moon[m1][-1]['vy'] = moon[m1][step]['vy']
        moon[m1][-1]['vz'] = moon[m1][step]['vz']

        for m2 in range(len(moon)):
            if moon[m1] == moon[m2]:
                continue

            if moon[m1][step]['px'] < moon[m2][step]['px']:
                moon[m1][-1]['vx'] += 1
            elif moon[m1][step]['px'] > moon[m2][step]['px']:
                moon[m1][-1]['vx'] -= 1

            if moon[m1][step]['py'] < moon[m2][step]['py']:
                moon[m1][-1]['vy'] += 1
            elif moon[m1][step]['py'] > moon[m2][step]['py']:
                moon[m1][-1]['vy'] -= 1

            if moon[m1][step]['pz'] < moon[m2][step]['pz']:
                moon[m1][-1]['vz'] += 1
            elif moon[m1][step]['pz'] > moon[m2][step]['pz']:
                moon[m1][-1]['vz'] -= 1

            moon[m1][-1]['px'] = moon[m1][step]['px'] + moon[m1][-1]['vx']
            moon[m1][-1]['py'] = moon[m1][step]['py'] + moon[m1][-1]['vy']
            moon[m1][-1]['pz'] = moon[m1][step]['pz'] + moon[m1][-1]['vz']

    for m in range(len(moon)):
        print("step: {}\tmoon: {}\tpx{}, py{}, pz{}, vx{}, vy{}, vz{}".format(
            step,
            m,
            moon[m][-1]['px'],
            moon[m][-1]['py'],
            moon[m][-1]['pz'],
            moon[m][-1]['vx'],
            moon[m][-1]['vy'],
            moon[m][-1]['vz']
        ))
    print()

    if  moon[0][-1] == bang[0][0] and moon[1][-1] == bang[1][0] and \
        moon[2][-1] == bang[2][0] and moon[3][-1] == bang[3][0]:
        print("found match after", step, "iterations")
        break

total_e = 0
for m in range(len(moon)):
    print( \
        "moon: {}\tpot: x{}, y{}, z{} = abs({})\tkin: x{}, y{}, z{} = abs({})\ttot: {} * {} = {}"
        .format(
        moon[m][-1]['name'],
        moon[m][-1]['px'], 
        moon[m][-1]['py'],
        moon[m][-1]['pz'],
        abs(moon[m][-1]['px']) + abs(moon[m][-1]['py']) + abs(moon[m][-1]['pz']),
        moon[m][-1]['vx'], 
        moon[m][-1]['vy'],
        moon[m][-1]['vz'],
        abs(moon[m][-1]['vx']) + abs(moon[m][-1]['vy']) + abs(moon[m][-1]['vz']),
        abs(moon[m][-1]['px']) + abs(moon[m][-1]['py']) + abs(moon[m][-1]['pz']),
        abs(moon[m][-1]['vx']) + abs(moon[m][-1]['vy']) + abs(moon[m][-1]['vz']),
        (abs(moon[m][-1]['px']) + abs(moon[m][-1]['py']) + abs(moon[m][-1]['pz'])) *
        (abs(moon[m][-1]['vx']) + abs(moon[m][-1]['vy']) + abs(moon[m][-1]['vz']))
        ))

    total_e += (abs(moon[m][-1]['px']) + abs(moon[m][-1]['py']) + abs(moon[m][-1]['pz'])) * \
        (abs(moon[m][-1]['vx']) + abs(moon[m][-1]['vy']) + abs(moon[m][-1]['vz']))

print ("sum total energy:", total_e, "after", iterations, "iterations")

#print(np.lcm(bang[0][0]['px'], bang[1][0]['px'], bang[2][0]['px'], bang[3][0]['px']))