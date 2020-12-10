#!/usr/bin/python3

find = 'shiny gold'

fh = open("input-test.txt", mode='r')
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


def searchr (key):
    global cntr
    global bags
    global find
    
    if find in bags.get(key).keys():
        cntr += 1
        return(True)
    else:
        for bag in bags.get(key).keys():
            if searchr(bag):
                return(True)
    

for bag in bags.keys(): searchr(bag)

print(cntr)