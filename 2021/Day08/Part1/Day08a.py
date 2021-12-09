#!/usr/bin/env python
"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
#!0:5 1:2 2:5 3:5 4:4 5:5 6:6 7:3 8:7 9:6

itxt = open("input", mode='r').read().strip().splitlines()
itxt = [i.split(' ') for i in itxt]

u = [[s for s in e[11:15] if len(s) in [2,4,3,7]] for e in itxt]
f = [j for sub in u for j in sub]
    
print(len(f))

