#!/usr/bin/env python

from icecream import ic
import sys
from functools import reduce

def main () -> int:

    games = {}

    itxt = open("input", mode='r').read().split('\n')
    
    ls = [ (int(l.split(': ')[0].split(' ')[1]), l.split(': ')[1].split('; ')) for l in itxt ]

    for k, v in ls:
        games[k] = [{ c.split(' ')[1]: int(c.split(' ')[0]) for c in vv.split(', ') } for vv in v]

    ggs = {}

    for g, rounds in games.items():
        ggs[g] = { 'red': [], 'green': [], 'blue': [] }
        
        for r in rounds:
            for c, n in r.items():
                ggs[g][c].append(n)
                
        ggs[g] = {c: max(ns) for c, ns in ggs[g].items()}

    #powers = [ reduce(lambda x, y: x * y, v.values()) for v in ggs.values() ]
    powers = [r['red'] * r['green'] * r['blue'] for g, r in ggs.items()]
            
    ic(sum(powers))

if __name__ == '__main__':
    sys.exit(main()) 
    
    