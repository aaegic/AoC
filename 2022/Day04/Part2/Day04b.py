#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()
    itxt = [i.split(',') for i in itxt]
    itxt = [j.split('-') for i in itxt for j in i]
    itxt = [(int(i[0]), int(i[1])) for i in itxt]
    
    num = 0
    
    for l,r in zip(itxt[0::2], itxt[1::2]):
        num += 1 if set(range(l[0],l[1]+1)) & set(range(r[0],r[1]+1)) else 0
        
    ic(num)


if __name__ == '__main__':
    sys.exit(main()) 
    
    