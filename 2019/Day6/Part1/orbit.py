#!/usr/bin/python3

""" CAVEAT: COM node must be on first line of input.txt """

from var_dump import var_dump

fh = open("input.txt", mode='r')
input_list = fh.read()
fh.close()

input_list = input_list.strip()
input_list = input_list.split("\n")


def findp(name, dict):
    for i, j in dict.items():
        for k in j:
            if k == name:
                return i


start = ""
orbit = {}
pdist = {}
pendn = []
paths = []

for i in input_list:
    _a, _b = i.split(")")
    if _a in orbit:
        orbit[_a].append(str(_b))
    else:
        orbit[_a] = []
        orbit[_a].append(str(_b))

    if not start:
        start = _a
        pdist[_a] = 0

for i, j in orbit.items():
    for k in orbit.get(i):
        if k not in orbit:
            pendn.append(k)

for i in pendn:
    p = []
    p.append(i)
    while i is not start:
        i = findp(i, orbit)
        p.append(i)
    paths.append(list(reversed(p)))

for i in paths:
    for j in range(len(i)):
        pdist[i[j]] = j

count = 0
for i, j in pdist.items():
    count = count + j

#var_dump(pdist)
print(count)
#print(orbit)

# {'COM': ['B'], 'B': ['C', 'G'], 'C': ['D'], 'D': ['E', 'I'], 'E': ['F', 'J'], 'G': ['H'], 'J': ['K'], 'K': ['L']}
# ict_items([('COM', ['B']), ('B', ['C', 'G']), ('C', ['D']), ('D', ['E', 'I']), ('E', ['F', 'J']), ('G', ['H']), ('J', ['K']), ('K', ['L'])])
