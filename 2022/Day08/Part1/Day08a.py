#!/usr/bin/env python

import sys

def main () -> None:

    last = lambda in_list: in_list[-1]

    itxt = open("input", mode='r').read().splitlines()
    tree = {(x,y): t for y, row in enumerate(itxt) for x, t in enumerate(list(row))}

    yr = range(1, len(itxt) - 1)
    xr = range(1, len(list(itxt)) - 1)
    
    visi = [(0, 0), (0, max(yr) + 1), (max(xr) + 1, 0), (max(xr) + 1, max(yr) + 1)]

    for y in yr: #l->r
        visi.append((0,y))
        for x in xr:
            if tree.get((x,y)) > tree.get(last(visi)):
                visi.append((x,y))
    
    for y in yr: #r->l
        visi.append((max(xr) + 1, y))
        for x in reversed(xr):
            if tree.get((x,y)) > tree.get(last(visi)):
                visi.append((x,y))

    for x in xr: #t->b
        visi.append((x,0))
        for y in yr: 
            if tree.get((x,y)) > tree.get(last(visi)):
                visi.append((x,y))

    for x in xr: #b->t
        visi.append((x, max(yr) + 1))
        for y in reversed(yr):
            if tree.get((x,y)) > tree.get(last(visi)):
                visi.append((x,y))

    print(len(set(visi)))


if __name__ == '__main__':
    sys.exit(main()) 
    
    