#!/usr/bin/python3

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

queue = intxt.split("\n")[1].split(",")
queue = filter(lambda x: x[1] != 'x', enumerate(queue))
queue = tuple(map(lambda x: (x[0], int(x[1])), queue))

time = 0
mult = 1

for delay, bus in queue:
    while (delay + time) % bus != 0:
        time += mult
    mult *= bus

print(time)
