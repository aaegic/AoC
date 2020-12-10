#!/usr/bin/python3

import sys

find = 'shiny gold'

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n")

bags = {}
cntr = 0

for line in intxt:
    line = line.replace(" bags", "")\
                .replace(" bag", "")\
                .replace(".", "")  

    parent, _c = line.split(" contain ")[0],\
                line.split(" contain ")[1].split(", ")

    children = {}
    
    for i in _c:
        if i == "no other": continue
        _c1, _c2 = i[0:i.find(" ")], i[i.find(" ")+1:]
        children.update({_c2: int(_c1)})
    
    bags.update({parent: children})


def tallyr (key):
    global bags
    _cnt = 0

    if len(bags.get(key).keys()) == 0: return 1
    
    _cnt += 1
    
    for bag in bags.get(key).keys():
        _cnt += bags.get(key).get(bag) * tallyr(bag)

    return _cnt 


print(tallyr(find) - 1) #subtract the shiny gold bag
