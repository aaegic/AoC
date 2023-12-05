#!/usr/bin/env python

from icecream import ic
import sys
from functools import reduce
from math import prod

def main () -> int:

    def get_num(x, y) -> dict:
        num = str()
        while x >= 0 and (x-1,y) in nums.keys():
            x -= 1
        
        lpos = x
        
        while (x,y) in nums.keys(): 
            num += nums[(x,y)]
            x += 1
            
        return {(lpos, y): int(num)}
        

    lines = open("input", mode='r').read().split('\n')
    
    gears = set()
    nums = dict()
    gear_parts = dict()
    
    for y, line in enumerate(lines):
        for x, d in enumerate(line):
            if d.isnumeric():
                nums.update({(x,y): str(d)})
            elif d == '*':
                gears.add((x,y))

    for x, y in gears:
        for sym in ((x-1,y-1),(x,y-1),(x-1,y),(x,y+1),(x+1,y),(x+1,y+1),(x-1,y+1),(x+1,y-1)):
            if sym in nums:
                if (x,y) not in gear_parts.keys():
                    gear_parts.update({(x,y): list()})
                    
                num = get_num(*sym)
                
                if num not in gear_parts[(x,y)]:
                    gear_parts[(x,y)].append(num)
    
    prods = list()
    
    for parts in gear_parts.values():
        if len(parts) < 2: continue
        
        nums = [ next(iter(part.values())) for part in parts ]
        prods.append(prod(nums))
    
    ic(sum(prods))
        

if __name__ == '__main__':
    sys.exit(main()) 
    
    