#!/usr/bin/python3

fh = open("input-test.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

stack = [0]
stack.extend(sorted(list(map(int, intxt))))
stack.append(stack[-1]+3)

ctack = [0]
ctack[0] = [0]

ncomb = 0

for i in stack:
    for j in range(len(ctack)):
        if i - ctack[j][-1] <= 3 and i - ctack[j][-1] > 0:
            mlist = ctack[j].copy()
            mlist.append(i)
            ctack.append(mlist)
            
        if i - ctack[j][-1] > 12  and i - ctack[j][-1] > 0:
            ctack.remove(ctack[j])

for i in range(len(ctack)):
    if ctack[i][0] == stack[0] and ctack[i][-1] == stack[-1]:
        ncomb += 1
        
print(ncomb)
