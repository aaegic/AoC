#!/usr/bin/env python

import sys
from icecream import ic

def main () -> int:

    itxt = open("input", mode='r').read().strip().splitlines()

    iq = {(i,j): {'$': int(v), 'v': None} for i, r in enumerate(itxt) for j, v in enumerate(r)} #input
    cq = dict() # $ed
    vq = dict() # visited
    last = (max([r for (r,c) in iq.keys()]), max([c for (r,c) in iq.keys()]))

    def getncs(r: int, c: int) -> set:
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]

    def getnns(nc:tuple, q:dict) -> set:
        return {ik: iv for ik, iv in q.items() if ik in getncs(*nc)}

    def qsrt(q:dict) -> set:
        return(dict(sorted(q.items(), key=lambda i: i[1]['$'])))

    def qget(q:dict) -> dict:
        q = qsrt(q)
        fk = list(q.keys())[0]
        fv = q.get(fk)
        del q[list(q.keys())[0]]
        return(({fk:fv},q))

    def qput(q:dict, i:dict) -> dict:
        q.update(i)
        return(q)

    cq = qput(cq,{(0,0):{'$': 0, 'v': None}})
    del iq[(0,0)]

    while len(iq):
        (p,cq) = qget(cq)
        pc = list(p.keys())[0]
        cost = p[pc]['$']

        for k,v in getnns(pc,iq).items():
            if cost <= v['$'] or v['v'] == None:
                cq = qput(cq,{k:{'$': cost + v['$'], 'v': pc}})
                del iq[k]
        
        vq = qput(vq,{pc:{'$': cost,'v': p[pc]['v']}})

    for k,v in cq.items():
        if k in vq.keys():
            if vq.get(k)['$'] < v['$']:
                vq = qput(vq,{k:{'$': v['$'], 'v': v['v']}})
        else:
            vq = qput(vq,{k:{'$': v['$'], 'v': v['v']}})

    print(vq.get(last,0)['$'])

    
if __name__ == '__main__':
    sys.exit(main()) 