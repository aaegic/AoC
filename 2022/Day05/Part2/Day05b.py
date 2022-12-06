#!/usr/bin/env python

from icecream import ic
import sys
from string import digits, ascii_uppercase

def main () -> int:

    """
        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """

    itxt = open("input", mode='r').read()
    itxt, moves = itxt.split('\n\n')
    moves = list(filter(lambda e: e not in ['move', 'from', 'to'], moves.split()))
    moves = list(map(int, moves))
    itxt = itxt.splitlines()
    
    stack_pos = itxt.pop(-1)
    itxt.reverse()
    
    stacks = dict()
    
    for i, e in enumerate(list(stack_pos)):
        if e in digits:
            stacks.update({ int(e): 
                [j[i] for j in itxt if j[i] in ascii_uppercase]})
    
    while len(moves):
        n = moves.pop(0) #number of crates
        f = moves.pop(0) #from stack
        t = moves.pop(0) #to stack
        
        h = [stacks[f].pop(-1) for _ in range(n)]
        h.reverse()
        
        stacks[t].extend(h)
        

    for i in stacks.values():
        print(i[-1], end='')


if __name__ == '__main__':
    sys.exit(main()) 
    
    