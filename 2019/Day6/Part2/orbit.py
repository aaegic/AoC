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
path_san = ''
path_you = ''
path_lcn = ''

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

for i in range(len(paths)):
    if "SAN" in paths[i]:
        path_san = i

    if "YOU" in paths[i]:
        path_you = i

d = set(paths[path_san]).symmetric_difference(set(paths[path_you]))

print(paths[path_san])
print(paths[path_you])
print(d)
print(len(d)-2)
