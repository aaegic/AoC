#!/usr/bin/env python

from icecream import ic
import sys
from functools import lru_cache, cache

def main () -> int:

    lines = open("input", mode='r').read().split('\n')

    games = { int(line.split(':')[0].split('Card')[1]): (  
                set( int(i) for i in line.split(':')[1].split('|')[0].replace('  ', ' ').split(' ')[1:-1] ),
                set( int(i) for i in line.split(':')[1].split('|')[1].replace('  ', ' ').split(' ')[1:]) )
                for line in lines }

    cards = int()
    
    # @lru_cache(maxsize=None, typed=False)
    def scratch(n):
        nonlocal cards 
        cards += 1
        for g in range(1, len(games[n][0] & games[n][1])+1):
            scratch(n+g)
    
    for n in games:
        scratch(n)
        
    ic(cards)
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    