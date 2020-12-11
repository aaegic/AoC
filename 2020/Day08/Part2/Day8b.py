#!/usr/bin/python3

import sys
from var_dump import var_dump

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

intcode = []

for line in intxt:
    [oc, oa] = line.split(' ')
    intcode.append({oc: int(oa)})


def run (intcode):
    acc = 0
    ptr = 0
    ptrlist = []

    while True:

        oc = list(intcode[ptr].keys())[0]
        oa = intcode[ptr].get(oc)

        if ptr in ptrlist:
            return False
        else:
            ptrlist.append(ptr)
        
        if oc == 'nop':
            ptr += 1
            
        if oc == 'acc': 
            acc += oa
            ptr += 1

        if oc == 'jmp':
            ptr += oa

        if ptr == len(intcode):
            print("SUCCESS", acc)
            sys.exit(0)


for ptr in range(len(intcode)):
    oc = list(intcode[ptr].keys())[0]  
    oa = intcode[ptr].get(oc)
    
    if oc == 'nop':
        oc = 'jmp'
    elif oc == 'jmp': 
        oc = 'nop'
    else: 
        continue
    
    intcode_c = intcode.copy()
    intcode_c[ptr] = {oc: oa}

    run(intcode_c)
    