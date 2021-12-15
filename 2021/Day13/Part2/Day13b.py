#!/usr/bin/env python

coords, fold = open("input", mode='r').read().split('\n\n')
coords = {(int(i[0]), int(i[1])) for i in [i.split(',') for i in coords.split()]}

fold = [{'axis':j.split('=')[0],'line':int(j.split('=')[1])} for j in \
    [i.split(' ')[2] for i in fold.split('\n')]]

origami = [list(coords)]

for f in fold:    
    no = set()
    for (x,y) in origami[-1]:
        if f['axis'] == 'y' and y > f['line']: 
            y = (2*f['line']) - y
            
        elif f['axis'] == 'x' and x > f['line']:
            x = (2*f['line']) - x
            
        no.add((x,y))
            
    origami.append(no)
    #Uncomment for part 1
    #break

last = {'x': max([i[0] for i in origami[-1]]), 'y': max([i[1] for i in origami[-1]])}
first = {'x': min([i[0] for i in origami[-1]]), 'y': min([i[1] for i in origami[-1]])}
    
for r in range(first['y'],last['y']+1):
    for c in range(first['x'],last['x']+1):
        if (c,r) in origami[-1]:
            print('▓', end='')
        else:
            print('░', end='')
            
    print('\n', end='')

print(len(origami[-1]))
"""
░▓▓░░▓▓▓░░▓░░▓░▓▓▓▓░▓▓▓░░░▓▓░░▓░░▓░▓░░▓
▓░░▓░▓░░▓░▓░░▓░░░░▓░▓░░▓░▓░░▓░▓░░▓░▓░░▓
▓░░▓░▓░░▓░▓▓▓▓░░░▓░░▓░░▓░▓░░░░▓░░▓░▓▓▓▓
▓▓▓▓░▓▓▓░░▓░░▓░░▓░░░▓▓▓░░▓░░░░▓░░▓░▓░░▓
▓░░▓░▓░▓░░▓░░▓░▓░░░░▓░░░░▓░░▓░▓░░▓░▓░░▓
▓░░▓░▓░░▓░▓░░▓░▓▓▓▓░▓░░░░░▓▓░░░▓▓░░▓░░▓
"""