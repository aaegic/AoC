#!/usr/bin/env python

from var_dump import var_dump
from icecream import ic
import sys
from functools import reduce

def main () -> int:

    itxt = open("input", mode='r').read().split('\n')

    total = 0

    for l in itxt:
        ns = list(filter(str.isnumeric, list(l)))
        total += int(ns[0] + list(reversed(ns))[0])

    # Golf...
    #total = sum([ int(list(filter(str.isnumeric, list(l)))[0] + list(reversed(list(filter(str.isnumeric, list(l)))))[0]) for l in itxt])

    ic(total)
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    