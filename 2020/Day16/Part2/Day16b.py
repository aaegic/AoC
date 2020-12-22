#!/usr/bin/python3

import itertools
import copy
import math

fh = open("input.txt")
intxt = fh.read()
fh.close()

sects = intxt.split("\n\n")
srule = sects[0].split("\n")
sytkt = sects[1].split("\n")[1:]
sntkt = sects[2].split("\n")[1:]
gdtkt = list()
altkt = list()
sntkt.extend(sytkt)

for i, tkt in enumerate(sntkt):
    tkt = list(map(int, tkt.split(',')))
    altkt.append(tkt)

rules = dict()

for r in srule:
    f1, f2 = r.split(':')
    f2 = f2.strip()
    r2, r3, r4 = f2.split(' ')
    r2min, r2max = r2.split('-')
    r4min, r4max = r4.split('-')
    rules.update({f1: {'r1min': int(r2min), 'r1max': int(r2max), \
        'r2min': int(r4min), 'r2max': int(r4max)}})

gdtkt = copy.deepcopy(altkt)

for tkt in altkt:
    for tf in tkt:
        valid_flag = False
        
        for rule in rules.values():
            if rule['r1min'] <= tf <= rule['r1max'] \
                    or rule['r2min'] <= tf <= rule['r2max']:
                valid_flag = True
                break
                
        if not valid_flag:
            gdtkt.remove(tkt)
            break

cname = dict()

for i in range(len(gdtkt[0])):
    cname.update({ i: list(rules.keys())})

sktcl = list(zip(*gdtkt))

for tkti, tktcl in enumerate(sktcl):
    for rname, rule in rules.items():
        for tf in tktcl:
            if not (rule['r1min'] <= tf <= rule['r1max'] \
                    or rule['r2min'] <= tf <= rule['r2max'] \
                    and rule['r1min'] <= tf <= rule['r1max'] \
                    or rule['r2min'] <= tf <= rule['r2max']):

                if rname in cname[tkti]:
                    cname[tkti].remove(rname)
    
while len(list(itertools.chain(*cname.values()))) > len(cname):
    for i, cns in cname.items():
        if len(cns) == 1:
            for j, cns2 in cname.items():
                if cns[0] in cns2 and i != j:
                    cns2.remove(cns[0])
                    cname.update({j: cns2})

sytkt = sytkt[0].split(',')
answer = list()

for i, cn in cname.items():
    if cn[0].startswith('depart'):
        answer.append(int(sytkt[i]))

print(math.prod(answer))
