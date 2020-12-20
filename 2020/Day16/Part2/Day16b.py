#!/usr/bin/python3

import copy

fh = open("input-test.txt")
intxt = fh.read()
fh.close()

sects = intxt.split("\n\n")
srule = sects[0].split("\n")
sytkt = sects[1].split("\n")[1:]
sntkt = sects[2].split("\n")[1:]
gdtkt = dict()
altkt = dict()
sntkt.extend(sytkt)

for i, tkt in enumerate(sntkt):
    tkt = list(map(int, tkt.split(',')))
    altkt.update({i: tkt})

rules = dict()

for i, r in zip(range(0, len(srule) + 2, 2), srule):
    print(r)
    f1, f2 = r.split(':')
    f2 = f2.strip()
    r2, r3, r4 = f2.split(' ')
    r2min, r2max = r2.split('-')
    r4min, r4max = r4.split('-')
    rules.update({f1: {'r1min': int(r2min), 'r1max': int(r2max), \
        'r2min': int(r4min), 'r2max': int(r4max)}})

gdtkt = copy.deepcopy(altkt)

for tkti in altkt.keys():
    tkt = altkt.get(tkti)
    
    for tf in tkt:
        valid_flag = False
        
        for rule in rules.values():
            if rule['r1min'] <= tf <= rule['r1max'] \
                    or rule['r2min'] <= tf <= rule['r2max']:
                valid_flag = True
                break
    
        if not valid_flag:
            del gdtkt[tkti]
            break

for i in gdtkt.items():
    print(i)
