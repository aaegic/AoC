#!/usr/bin/python3

from var_dump import var_dump
import math
from collections import defaultdict

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n\n")

goodpass = 0

for l in intxt:
    p = l.replace(" ", "\n")
    pc = len(p.split("\n"))
    
    if pc == 8 or (pc >= 7 and p.find("cid:") == -1):
        goodpass += 1
        
print(goodpass)