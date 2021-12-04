#!/usr/bin/env python
#1800151
from var_dump import var_dump

fh = open("input-test", mode='r')
intxt = fh.read()
fh.close()

intxt = list(intxt.strip().split("\n"))

intxt = list(map(list, intxt))
intxt = [list(map(int, i)) for i in intxt]

#pass by reference
#diag = intxt
diag = list(intxt)




while len(diag) > 1:

    #transpose
    diag_t = list(map(list, zip(*diag)))

    nbit = [sum(i) for i in diag_t]
    mcbs = [1 if i >= (len(diag_t[0]) / 2) else 0 for i in nbit]



    for i in range(len(mcbs)):
        for j in range(len(diag)):
            if mcbs[i] != diag[j][i]:
                diag.pop(j)
                break
        else:
            continue
        break
#100111101011
o2 = ''.join(map(str, diag[0]))
