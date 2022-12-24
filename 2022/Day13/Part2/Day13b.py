#!/usr/bin/env python

import sys
from itertools import zip_longest

def main () -> None:

    def compare(l, r) -> bool:
        for ll, rr in zip_longest(l, r, fillvalue=None):
            if ll == None: return True
            if rr == None: return False
            
            if isinstance(ll, int) and isinstance(rr, int):
                if ll > rr: return False
                if ll < rr: return True
            else:
                if isinstance(rr, int): rr = [rr]
                if isinstance(ll, int): ll = [ll]
                
                ret = compare(ll, rr)
                if ret in [True, False]: return ret #continue on None
                

    itxt = open("input", mode='r').read().split("\n\n")
    itxt = [i.splitlines() for i in itxt]
    pkts = [ eval(j) for i in itxt for j in i ] + [[[2]],[[6]]]

    while True: #.oO(...)
        for i in range(len(pkts)-1):
            if compare(pkts[i], pkts[i+1]) == False:
                pkts[i], pkts[i+1] = pkts[i+1], pkts[i]
                done = False

        if done == True: break
        done = True

    print((pkts.index([[2]]) + 1) * (pkts.index([[6]]) + 1))


if __name__ == '__main__':
    sys.exit(main()) 
    