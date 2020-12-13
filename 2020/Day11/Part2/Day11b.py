#!/usr/bin/python3

from copy import deepcopy

fh = open("input-test.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip().split("\n")
f = list(list(r) for r in intxt)

def showf (f): [ print(r) for r in f ]

def cntocc (f): return sum([ r.count("#") for r in f ])

def cntadj (r, c, f):
    adj = 0
    
    for dd in range(1, len(f)):
        if r - dd < 0 or c - dd < 0:
            break
        if f[r-dd][c-dd] == "#":
            adj += 1
            break        
        if f[r-dd][c-dd] == "L":
            break      
    
    if r > 0: #up
        for dr in range(1, len(f) - r + 1):
            if f[r-dr][c] == "#":
                adj += 1
                break
            if f[r-dr][c] == "L":
                break
    
    if r > 0 and c < len(f[r]) - 1: adj += f[r-1][c+1].count("#")
    
    if c > 0: #left
        for dc in range(1, len(f) - c + 1):
            if f[r][c-dc] == "#":
                adj += 1
                break
            if f[r][c-dc] == "L":
                break
                
    if c < len(f) - 1: #right
        for dc in range(1, len(f) - c):
            if f[r][c+dc] == "#":
                adj += 1
                break
            if f[r][c+dc] == "L":
                break
    
    if r < len(f) - 1 and c > 0: adj += f[r+1][c-1].count("#")
    
    if r < len(f) - 1: #down
        for dr in range(1, len(f) - r):
            if f[r+dr][c] == "#":
                adj += 1
                break
            if f[r+dr][c] == "L":
                break
    
    if r < len(f) - 1 and c < len(f[r]) - 1: adj += f[r+1][c+1].count("#")
    
    return(adj)
    

def part1 (f):
    _f = deepcopy(f)
    
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] == "L" and cntadj(r, c, f) == 0:
                _f[r][c] = "#"
            elif f[r][c] == "#" and cntadj(r, c, f) >= 5:
                _f[r][c] = "L"
                
    return(_f)


print(cntadj(9,9, f))


"""
f2 = []
f1 = part1(tuple(f))

while f1 != f2:
    f2 = deepcopy(f1)    
    f1 = part1(tuple(f1))

showf(f1)
print(cntocc(f1))
"""