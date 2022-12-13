#!/usr/bin/env python

import sys

def main () -> None:

    itxt = open("input", mode='r').read().splitlines()
    itxt = [i.split() for i in itxt]

    x = 1
    clk = 0
    signal = list()

    def incclk():
        nonlocal x, clk, signal
        
        clk += 1
        
        if clk == 20 or (clk - 20) %40 == 0:
            signal.append(clk * x)
        
    for ins in itxt:
        if ins[0] == 'noop':
            incclk()
        elif ins[0] == 'addx':
            incclk()
            incclk()
            x += int(ins[1])
            
    print(sum(signal))
    
    
if __name__ == '__main__':
    sys.exit(main()) 
    