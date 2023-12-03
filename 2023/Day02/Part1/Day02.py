#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    m = { 'red': 12, 'green': 13, 'blue': 14 }
    gs = {}

    itxt = open("input", mode='r').read().split('\n')
    
    ls = [ (int(l.split(': ')[0].split(' ')[1]), l.split(': ')[1].split('; ')) for l in itxt ]

    for k, v in ls:
        gs[k] = [{ c.split(' ')[1]: int(c.split(' ')[0]) for c in vv.split(', ') } for vv in v]

    gsn = set(gs.keys())
            
    for g, rs in gs.items():
        for r in rs:
            for c, n in r.items():
                if n > m[c]:
                    gsn.discard(g)

    ic(sum(gsn))

if __name__ == '__main__':
    sys.exit(main()) 
    
    