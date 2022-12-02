#!/usr/bin/env python

from var_dump import var_dump
from icecream import ic
import sys

def main () -> int:

    itxt = open("input", mode='r').read().split('\n\n')

    itxt = [i.strip().split('\n') for i in itxt]

    itxt = sorted([sum(list(map(int, i))) for i in itxt])
    
    itxt.reverse()
    
    ic(next(iter(itxt)))
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    