#!/usr/bin/env python

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

intxt = list(intxt.strip().split("\n"))

intxt = list(map(list, intxt))
intxt = [list(map(int, i)) for i in intxt]

#pass by reference
#diag = intxt
#pass by value
diag = list(intxt)

#o2
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
        #python-esque break 2
        else:
            continue
        break

o2 = ''.join(map(str, diag[0]))

diag = list(intxt)

"""
the above works for o2 section but not for co2 ¯\_(ツ)_/¯
"""

#co2
for i in range(len(diag[0])):
    #transpose
    diag_t = list(map(list, zip(*diag)))

    #nested list comprehension
    lcbs = [0 if i >= (len(diag_t[0]) / 2) else 1 for i in [sum(i) for i in diag_t]]

    remv = [diag[j] for j in range(len(diag)) if lcbs[i] != diag[j][i]]
    [diag.remove(r) for r in remv if len(diag) > 1]

co2 = ''.join(map(str, diag[0]))

print(int(o2, 2) * int(co2, 2))

