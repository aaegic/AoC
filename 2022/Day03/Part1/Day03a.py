#!/usr/bin/env python

from var_dump import var_dump
from icecream import ic
import sys
from string import ascii_lowercase
from string import ascii_uppercase

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()
    itxt = [list(i) for i in itxt]
    
    cc = list()
    
    for i in itxt:
        c0 = i[0:int(len(i)/2)]
        c1 = i[(int(len(i)/2)):]    
        cc.append([c for c in c0 if c in c1][0])
    
    ic(sum([list(ascii_lowercase + ascii_uppercase).index(c)+1 for c in cc]))
        

if __name__ == '__main__':
    sys.exit(main()) 
    
    