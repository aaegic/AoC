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
    
    lend = len(f) if len(f) > len(f[r]) else len(f[r])
    
    for dd in range(1, lend): #up left
        if r - dd < 0 or c - dd < 0:
            break
        if f[r-dd][c-dd] == "L":
            break
        if f[r-dd][c-dd] == "#":
            adj += 1
            break

    for dd in range(1, lend): #down right
        if r + dd > len(f) - 1 or c + dd > len(f[r]) - 1:
            break
        if f[r+dd][c+dd] == "L":
            break
        if f[r+dd][c+dd] == "#":
            adj += 1
            break

    for dd in range(1, lend): #down left
        if r + dd > len(f) - 1 or c - dd < 0:
            break
        if f[r+dd][c-dd] == "L":
            break
        if f[r+dd][c-dd] == "#":
            adj += 1
            break
        
    for dd in range(1, lend): #up right
        if r - dd < 0 or c + dd > len(f[r]) - 1:
            break
        if f[r-dd][c+dd] == "L":
            break
        if f[r-dd][c+dd] == "#":
            adj += 1
            break
    
    for dr in range(1, len(f)): #up
        if r - dr < 0:
            break
        if f[r-dr][c] == "L":
            break
        if f[r-dr][c] == "#":
            adj += 1
            break
    
    for dc in range(1, len(f[r])): #left
        if c - dc < 0:
            break
        if f[r][c-dc] == "L":
            break
        if f[r][c-dc] == "#":
            adj += 1
            break

    for dc in range(1, len(f[r])): #right
        if c + dc > len(f[r]) - 1:
            break
        if f[r][c+dc] == "L":
            break
        if f[r][c+dc] == "#":
            adj += 1
            break

    for dr in range(1, len(f)): #down
        if r + dr > len(f) - 1:
            break
        if f[r+dr][c] == "L":
            break
        if f[r+dr][c] == "#":
            adj += 1
            break
    
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


f2 = []
f1 = part1(tuple(f))

while f1 != f2:
    f2 = deepcopy(f1)    
    f1 = part1(tuple(f1))

#showf(f1)
print(cntocc(f1))
