#!/usr/bin/env python

from itertools import pairwise

ipoly, pairs = open("input", mode='r').read().split('\n\n')
pairs = {j[0]:j[1] for j in [i.split(' -> ') for i in pairs.split('\n')]}

elements = dict()
polymers = dict()

for p in list(ipoly):
    elements.update({p: elements.get(p,0)+1})

for p in pairwise(ipoly):
    polymers.update({''.join(p): polymers.get(''.join(p),0) + 1})

for i in range(40):
    polymers2 = dict()
    for pk, pv in polymers.items():
        pe1, pe2 = list(pk)

        polymers2.update({''.join([pe1,pairs[pk]]): polymers2.get(''.join([pe1,pairs[pk]]),0) +pv})
        polymers2.update({''.join([pairs[pk],pe2]): polymers2.get(''.join([pairs[pk],pe2]),0) +pv})
        elements.update({pairs[pk]: elements.get(pairs[pk],0) + pv})

    polymers = dict(polymers2)

dvs = list(dict(sorted(elements.items(), key=lambda i: i[1])).values())
print(dvs[-1]-dvs[0])
