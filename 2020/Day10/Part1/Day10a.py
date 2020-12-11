#!/usr/bin/python3

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

stack = [0]
stack.extend(sorted(list(map(int, intxt))))
stack.append(stack[-1]+3)

deltas = {1: 0, 2: 0, 3: 0}

for i in range(1, len(stack)):
    d = stack[i] - stack[i-1]
    deltas[d] = deltas.get(d) + 1

print(deltas)
print(deltas.get(1) * deltas.get(3))
