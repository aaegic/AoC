#!/usr/bin/env python

from var_dump import var_dump

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

intxt = list(intxt.strip().split("\n"))
ins = [tuple(i.split(' ')) for i in intxt]

pos = { 'a': 0, 'x': 0, 'y': 0 }

for i, j in ins:
    match i:
        case 'forward':
            pos.update({'x': pos['x'] + int(j)})
            pos.update({'y': pos['y'] + (pos['a'] * int(j))})
        case 'up':
            pos.update({'a': pos['a'] - int(j)})
        case 'down':
            pos.update({'a': pos['a'] + int(j)})
        
print(pos, pos['x'] * pos['y'])

