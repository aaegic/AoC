#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    def get_num(x, y) -> int:
        num = str()
        while x >= 0 and (x-1,y) in nums.keys():
            x -= 1
        
        lpos = x
        
        while (x,y) in nums.keys(): 
            num += nums[(x,y)]
            x += 1
            
        return {(lpos, y): int(num)}
        

    lines = open("input", mode='r').read().split('\n')
    
    syms = set()
    nums = dict()
    parts = list()
    
    for y, line in enumerate(lines):
        for x, d in enumerate(line):
            if d == '.': continue
            if d.isnumeric():
                nums.update({(x,y): str(d)})
            else:
                syms.add((x,y))

    for x, y in syms:
        for sym in ((x-1,y-1),(x,y-1),(x-1,y),(x,y+1),(x+1,y),(x+1,y+1),(x-1,y+1),(x+1,y-1)):
            if sym in nums:
                num = get_num(*sym)
                if num not in parts:
                    parts.append(num)
    
    ic(sum([ p for part in parts for p in part.values()]))
        

if __name__ == '__main__':
    sys.exit(main()) 
    
    