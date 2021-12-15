#!/usr/bin/env python

def hasdup(p: list) -> bool:
    cnt = dict()

    for i in [l for l in p if l.islower()]:
        cnt[i] = cnt.get(i,0) +1
    
    if 3 in cnt.values() or len([i for i in cnt.values() if i == 2]) > 1:
        return True
    
    return False

def walk(room: str, path: list) -> list:
    path.append(room)
    
    if 'end' in path:
        paths.append(path)
        return path
    
    for r in rmap[room]:
        if hasdup(path) or r == 'start':
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
