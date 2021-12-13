#!/usr/bin/env python

def walk(room: str, path: list) -> list:
    path.append(room)
    
    if 'end' in path:
        paths.append(path)
        return path
    
    for r in rmap[room]:
        if r.islower() and r in path:
            continue
        
        #recursion
        #pass by reference pass by value make a list() or you'll be sorry
        walk(r, list(path))


itxt = [i.split('-') for i in open("input", mode='r').read().split()]
rmap = {a: {b} for a, b in itxt}
rmap.update({b: {a} for a, b in itxt})

for a, b in itxt:
    rmap[a].add(b)
    rmap[b].add(a)

paths = list()

path = walk('start', [])

print(len(paths))
