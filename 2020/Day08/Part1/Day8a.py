#!/usr/bin/python3

import sys
from var_dump import var_dump


fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

intcode = []
acc = 0
ptr = 0
ptrlist = []

for line in intxt:
    [oc, oa] = line.split(' ')
    intcode.append({oc: int(oa)})

while True:

    oc = list(intcode[ptr].keys())[0]
    oa = intcode[ptr].get(oc)

    if ptr in ptrlist:
        print(acc)
        sys.exit(0)
    else:
        ptrlist.append(ptr)
    
    if oc == 'nop':
        ptr += 1
        
    if oc == 'acc': 
        acc += oa
        ptr += 1

    if oc == 'jmp':
        ptr += oa




