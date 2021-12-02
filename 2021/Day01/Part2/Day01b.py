#!/usr/bin/env python

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

dms = list(map(int, intxt.strip().split("\n")))

#n = 0
#rngs = list()

#for i in range(2, len(dms), 1):
#    rngs.append(dms[i] + dms[i-1] + dms[i-2])

#for i in range(1, len(rngs), 1):
#    if rngs[i] > rngs[i-1]:
#        n += 1
#
#print(n)

#equivalent using list comprehension
rngs = [dms[i] + dms[i-1] + dms[i-2] for i in range(2, len(dms), 1)]
ns = [i for i in range(1, len(rngs), 1) if rngs[i] > rngs[i-1]]

print(len(ns))

