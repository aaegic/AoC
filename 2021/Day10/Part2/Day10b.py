#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()
T = [list(i) for i in itxt]

p = dict({'(': ')', '[': ']', '{': '}', '<': '>'})
pts = dict({ ')': 1, ']': 2, '}': 3, '>': 4 })

s = list()
ss = list()

for ln, L in enumerate(T):
    scr = 0
    
    for cn, C in enumerate(L):
        if C in p.keys():
            s.append(C)
        elif C in p.values():
            if C == p.get(s[-1]):
                s.pop()
            else:
                s = []
                break

    while len(s):
        scr = (scr * 5) + pts.get(p.get(s.pop()))
    
    if scr:
        ss.append(scr)

ss.sort()
# "rounding up" in Python
i = -(-(len(ss)) // 2) 

print(ss[i-1])
