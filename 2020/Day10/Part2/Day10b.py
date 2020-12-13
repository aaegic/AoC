#!/usr/bin/python3

from functools import lru_cache

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

stack = [0]
stack.extend(sorted(list(map(int, intxt))))
stack.append(stack[-1]+3)

@lru_cache(maxsize = 1000)
def pathr (ptr, stack):
    npath = 0

    if stack[-1] == stack[ptr]: return 1
    
    for n in range(len(stack)):
        if ptr+n < len(stack):
            if 0 < stack[ptr+n] - stack[ptr] <= 3:
                npath += pathr(ptr+n, stack)

    return npath

print(stack)
print(pathr(0, tuple(stack)))
