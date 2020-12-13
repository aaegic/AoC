#!/usr/bin/python3

from copy import deepcopy

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip().split("\n")
f = list(list(r) for r in intxt)

def showf (f): [ print(r) for r in f ]

def cntocc (f): return sum([ r.count("#") for r in f ])

def cntadj (r, c, f):
    adj = 0
    
    if r > 0 and c > 0: adj += f[r-1][c-1].count("#")
    if r > 0: adj += f[r-1][c].count("#")
    if r > 0 and c < len(f[r]) - 1: adj += f[r-1][c+1].count("#")
    if c > 0: adj += f[r][c-1].count("#")
    if c < len(f[r]) - 1: adj += f[r][c+1].count("#")
    if r < len(f) - 1 and c > 0: adj += f[r+1][c-1].count("#")
    if r < len(f) - 1: adj += f[r+1][c].count("#")
    if r < len(f) - 1 and c < len(f[r]) - 1: adj += f[r+1][c+1].count("#")
    
    return(adj)
    

def part1 (f):
    _f = deepcopy(f)
    
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] == "L" and cntadj(r, c, f) == 0:
                _f[r][c] = "#"
            elif f[r][c] == "#" and cntadj(r, c, f) >= 4:
                _f[r][c] = "L"
                
    return(_f)


f2 = []
f1 = part1(tuple(f))

while f1 != f2:
    f2 = deepcopy(f1)    
    f1 = part1(tuple(f1))

#showf(f1)
print(cntocc(f1))
