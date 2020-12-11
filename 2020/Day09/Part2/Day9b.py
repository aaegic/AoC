#!/usr/bin/python3

preamble = 25

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")
stack = list(map(int, intxt))

def part1 (stack, preamble):
    for i in range(preamble, len(stack)):
        for j in stack[i - preamble: i]:
            if stack[i] - j in stack[i - preamble: i]:
                break
        else:
            return(i)


ti = part1(stack, preamble)

print(stack[ti])

for si in range(ti):
    for ei in range(si, ti):
        if sum(stack[si:ei]) == stack[ti]:
            stran = sorted(stack[si:ei])
            print(stran)
            print(stran[0] + stran[-1])
            