#!/usr/bin/env python

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

intxt = list(intxt.strip().split("\n"))
ins = [tuple(i.split(' ')) for i in intxt]

pos = { 'x': 0, 'y': 0 }

for i, j in ins:
    match i:
        case 'forward':
            pos.update({'x': pos['x'] + int(j)})
        case 'up':
            pos.update({'y': pos['y'] - int(j)})
        case 'down':
            pos.update({'y': pos['y'] + int(j)})
        
print(pos, pos['x'] * pos['y'])

