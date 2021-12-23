#!/usr/bisn/env python

from var_dump import var_dump
from pprint import pprint
import sys
from icecream import ic
import heapq

def main () -> int:

    itxt = open("input-test", mode='r').read().strip().splitlines()

    iq = {(i,j): {'$': int(v), 'v': None} for i, r in enumerate(itxt) for j, v in enumerate(r)} #input
    cq = dict() # $ed
    vq = dict() # visited
    last = (max([r for (r,c) in iq.keys()]), max([c for (r,c) in iq.keys()]))

    def getncs(r: int, c: int) -> set:
        #return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r+1,c-1),(r-1,c+1)] \
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]

    def getnns(nc:tuple, q:dict) -> set:
        #q = {ik: iv for ik, iv in q.items() if ik in getncs(*nc)}
        return {ik: iv for ik, iv in q.items() if ik in getncs(*nc)}
        #return(dict(sorted(q.items(), key=lambda i: i[1]['$'])))
        return(qsrt(q))

    def qsrt(q:dict) -> set:
        return(dict(sorted(q.items(), key=lambda i: i[1]['$'])))

    def qget(q:dict) -> dict:
        q = qsrt(q)
        fk = list(q.keys())[0]
        fv = q.get(fk)
        del q[list(q.keys())[0]]
        return(({fk:fv},q))

    def qput(q:dict, i:dict) -> dict:
        #if list(i.keys())[0] in q: del q[list(i.keys())[0] ]
        q.update(i)
        #return(dict(qsrt(q)))
        #return(qsrt(q))
        return(q)

    cq = qput(cq,{(0,0):{'$': 0, 'v': None}})
    del iq[(0,0)]
    #vq = qput(vq,{(0,0):{'$': 0, 'v': None}})

    ic(cq)
    ic(vq)

    while len(iq):
        
        (p,cq) = qget(cq)
        pc = list(p.keys())[0]
        #ic(p, cq,pc)
        cost = p[pc]['$']
        nns = getnns(pc,iq)
        #ic(nns,cost)

        for k,v in nns.items():
            #ic(k,v, v['$'], nns[k]['$'])
            if cost <= nns[k]['$'] or nns[k]['v'] == None:
                cq = qput(cq,{k:{'$': cost + nns[k]['$'], 'v': pc}})
                del iq[k]
                #ic(cq)
        
        vq = qput(vq,{pc:{'$': cost,'v': p[pc]['v']}})
        #del iq[pc]

        xxx = cq.get(last,0)
        if xxx: ic(xxx)

        

    ic(iq,cq)
    
    quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    quit()

    paths = list()

    def getns(r: int, c: int) -> set:
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r+1,c-1),(r-1,c+1)] \
            if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]

    def getvs(np) -> set:
        nd = {ik: iv for ik, iv in rmap.items() if ik in getns(*np)}
        nd = list(dict(sorted(nd.items(), key=lambda i: i[1])))
        return(nd)


    def walk(pos: str, path: list) -> list:
        path.append(pos)
        
        if last in path:
            paths.append(path)
            return path
        
        for p in getvs(pos):
            #recursion
            #pass by reference pass by value make a list() or you'll be sorry
            walk(p, tuple(path))

    pos = (0,0)

    walk(pos, [])

    #risk = [sum([rmap.get(j) for j in i]) for i in paths]

if __name__ == '__main__':
    sys.exit(main()) 