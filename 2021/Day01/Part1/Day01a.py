#!/usr/bin/env python

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

dms = list(map(int, intxt.strip().split("\n")))

n = 0

for i in range(1, len(dms), 1):
    if dms[i] > dms[i-1]:
        n += 1
    
print(n)