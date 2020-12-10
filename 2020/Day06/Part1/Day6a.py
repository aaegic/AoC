#!/usr/bin/python3

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n\n")

count = 0

for group in intxt:
    npeople = len(group.split("\n"))
    
    allchar = group.replace("\n", "")
    
    cntchar = dict((i, allchar.count(i)) for i in allchar)
    count += list(cntchar.values()).count(npeople)
    
print(count)