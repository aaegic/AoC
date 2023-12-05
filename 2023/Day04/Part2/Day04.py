#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    lines = open("input", mode='r').read().split('\n')

    games = { int(line.split(':')[0].split('Card')[1]): (  
                set( int(i) for i in line.split(':')[1].split('|')[0].replace('  ', ' ').split(' ')[1:-1] ),
                set( int(i) for i in line.split(':')[1].split('|')[1].replace('  ', ' ').split(' ')[1:]) )
                for line in lines }

    cards = int()
    
    def scratch(n, c):
        c += 1
        for g in range(1, len(games[n][0] & games[n][1])+1):
            c = scratch(n+g, c)
            
        return c
    
    for n in games:
        cards += scratch(n, 0)
        
    ic(cards)
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    