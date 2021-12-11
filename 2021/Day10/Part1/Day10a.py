#!/usr/bin/env python

itxt = open("input", mode='r').read().strip().splitlines()
T = [list(i) for i in itxt]

p = dict({'(': ')', '[': ']', '{': '}', '<': '>'})
s = list()

ic = list()
pts = dict({ ')': 3, ']': 57, '}': 1197, '>': 25137 })

for ln, L in enumerate(T):
    for cn, C in enumerate(L):
        if C in p.keys():
            s.append(C)
        elif C in p.values():
            if C == p.get(s[-1]):
                s.pop()
            else:
                ic.append(C)
                break

score = sum([pts.get(c) for c in ic])
print(score)
