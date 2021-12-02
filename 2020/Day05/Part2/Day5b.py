#!/usr/bin/python3

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

sids = []

for line in intxt:
    rob = line[0:7].replace('F', '0').replace('B', '1')
    row = int(rob, 2)
    cob = line[7:].replace('L', '0').replace('R', '1')
    col = int(cob, 2)
    
    sid = (row * 8) + col
    sids.append(sid)
    
sids.sort()

for i in range(len(sids)):
    if i != 0 and sids[i] != sids[i-1]+1:
        print(sids[i] - 1)
