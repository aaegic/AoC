#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    # mjqjpqmgbljsphdztnvjfqwrcgsmlb

    itxt = open("input", mode='r').read()

    buf = list(itxt[0:3])
    
    for i, v in enumerate(itxt):
        buf += v
        
        if len(set(buf)) == 4:
            ic(i+1)
            return

        buf.pop(0)
        

if __name__ == '__main__':
    sys.exit(main()) 
    
    