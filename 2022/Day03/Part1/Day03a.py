#!/usr/bin/env python

from icecream import ic
import sys
from string import ascii_lowercase, ascii_uppercase

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()
    itxt = [list(i) for i in itxt]
    
    chars = list(ascii_lowercase + ascii_uppercase)
    cc = list()

    #illegible version
    #cc = [[c for c in i[0:len(i)//2] if c in i[(len(i)//2):]][0] for i in itxt]
        
    for i in itxt:
        c0 = i[0:len(i)//2]
        c1 = i[(len(i)//2):] 
        cc.append([c for c in c0 if c in c1][0])
    
    ic(sum([chars.index(c)+1 for c in cc]))
    

if __name__ == '__main__':
    sys.exit(main()) 
