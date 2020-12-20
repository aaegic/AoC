#!/usr/bin/python3

stop = 2020
stop = 30000000

#ipt = [ 0,3,6 ]
ipt = [ 8,11,0,19,1,2 ]

mem = dict()

for i, n in enumerate(ipt, 1):
    mem.update({n: {'pi': i}})
else:
    n = 0

for i in range(i + 1, stop):
    if mem.__contains__(n):
        ppi = mem.get(n).get('pi')
        mem.update({n: {'pi': i, 'ppi': ppi}})
        n = i - ppi
    else:     
        mem.update({n: {'pi': i, 'ppi': 0}})
        n = 0
    
    if (i + 1) % 10000 == 0: print(i + 1, n)
    
print(n)

