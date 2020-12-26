#!/usr/bin/python3

import itertools

fh = open("input-test.txt")
eq = fh.read()
fh.close()

#eq = "2 * 3 + (4 * 5)".replace(' ', '') # 26
#eq = "5 + (8 * 3 + 9 + 3 * 4 * 3)".replace(' ', '') # 437
#eq = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))".replace(' ', '') # 12240
#eq = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2".replace(' ', '') # 13632
#eq = "(8 + (7 + 9)) * 6".replace(' ', '')

def rindex(li:list, ch:str, lrange:int, rrange:int) -> int:
    for i in range(rrange, lrange - 1, -1):
        if li[i] == ch:
            return i

def compute():


eqlst = list()
reslt = list()

for line in eq.split("\n"):
    eq = list()
    for char in line.replace(' ', ''):
        if char == ' ':
            continue
        if char.isdigit():
            eq.append(int(char))
        else:
            eq.append(char)
    
    eqlst.append(eq)

print(eqlst)

eq = eqlst[3]

while '(' in eq:
    lft, opr = None, None
    
    rpi = eq.index(')')
    lpi = rindex(eq, '(', 0, rpi)

    print(eq)
    print(rpi, eq[rpi], lpi, eq[lpi])

    for e in eq[lpi+1:rpi]:
        if opr is not None:
            if opr == '+':
                lft = lft + e
            elif opr == '*':
                lft = lft * e
            
            opr = None
        elif lft is not None:
            opr = e
        else:
            lft = e

    eq = list(itertools.chain(eq[:lpi], [lft], eq[rpi+1:]))
    lft, opr = None, None

print(eq)

for e in eq:
    if opr is not None:
        if opr == '+':
            lft = lft + e
        elif opr == '*':
            lft = lft * e
        
        opr = None
    elif lft is not None:
        opr = e
    else:
        lft = e

eq = lft

print(eq)