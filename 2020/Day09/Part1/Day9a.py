#!/usr/bin/python3

preamble = 25

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")
stack = list(map(int, intxt))

for i in range(preamble, len(stack)):
    for j in stack[i - preamble: i]:
        if stack[i] - j in stack[i - preamble: i]:
            break
    else:
        print(stack[i])
        break
