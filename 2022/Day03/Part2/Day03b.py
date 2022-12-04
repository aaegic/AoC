#!/usr/bin/env python

from icecream import ic
import sys
from string import ascii_lowercase, ascii_uppercase

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()
    itxt = [list(i) for i in itxt]
    
    chars = list(ascii_lowercase + ascii_uppercase)
    badges = list()
    
    for i in range(0,len(itxt),3):
        elf0 = itxt[0+i]
        elf1 = itxt[1+i]
        elf2 = itxt[2+i]
        
        badge = list(set(elf0) & set(elf1) & set(elf2))[0]
        badges.append(badge)
    
    ic(sum([chars.index(b)+1 for b in badges]))


if __name__ == '__main__':
    sys.exit(main()) 
    
    