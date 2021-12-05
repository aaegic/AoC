#!/usr/bin/env python

fh = open("input", mode='r')
intxt = fh.read()
fh.close()

intxt = list(intxt.strip().split("\n"))

data = list(map(list, intxt))
data = [list(map(int, i)) for i in data]

#transpose
data = list(map(list, zip(*data)))

nbit = [sum(i) for i in data]

gamma = [1 if i > (len(data[0]) / 2) else 0 for i in nbit]
epsil = [0 if i > (len(data[0]) / 2) else 1 for i in nbit]

gamma = ''.join(map(str, gamma))
epsil = ''.join(map(str, epsil))

print(int(gamma, 2) * int(epsil, 2))
