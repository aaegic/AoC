#!/usr/bin/env python

from typing import Counter

poly, pair = open("input", mode='r').read().split('\n\n')

pair = {j[0]:j[1] for j in [i.split(' -> ') for i in pair.split('\n')]}

poly = [list(poly)]

for s in range(10):
    np = [poly[-1][0]]
    for i in (range(1,len(list(poly[-1])))):
        ins = pair.get(''.join([poly[-1][i-1],poly[-1][i]]))
        np.append(ins)
        np.append(poly[-1][i])

    poly.append(np)

dvs = list(dict(sorted(Counter(poly[-1]).items(), key=lambda i: i[1])).values())
print(dvs[-1]-dvs[0])
