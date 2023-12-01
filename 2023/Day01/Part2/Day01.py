#!/usr/bin/env python

from icecream import ic
import sys

def main () -> int:

    itxt = open("input", mode='r').read().split('\n')

    total = 0

    also_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    for l in itxt:
        ns = list()
        
        for i in range(len(l)):
            
            if l[i].isnumeric():
                ns.append(l[i])
                continue
            
            for k, v in also_numbers.items():
                if l[i:i + len(k)] == k:
                    ns.append(str(v))
                    
        total += int(ns[0] + list(reversed(ns))[0])

    ic(total)
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    