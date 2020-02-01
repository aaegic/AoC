#!/usr/bin/python3

from var_dump import var_dump
import pprint
import math
import numpy as np
from collections import defaultdict
import collections
from operator import itemgetter


def makehash():
    return collections.defaultdict(makehash)


def nncm(_yield, _qty):
    for i in range(0, (_yield * _qty) + 1):
        if i % _yield == 0 and i >= _qty:
            return i

r_table = []
e_table = defaultdict(int)
t_table = []

fh = open("input-demo1.txt", mode='r')

for i in fh:
    i = i.strip()
    l, r = i.split('=>')
    r = r.strip()

    qty, name = r.split(' ')
    r_table.append({ 'name': name, 'yield': int(qty), 'elmnt': {} })

    l = l.split(',')

    for j in l:
        j = j.strip()
        qty, name = j.split(' ')
        r_table[-1]['elmnt'].update({ name: int(qty) })

fh.close()

var_dump(r_table)

def c_ore(ename, qty = 1, cname = 'default'):
    global r_table
    global e_table

    print("c_core:", ename, qty)

    for e in r_table:
        if e['name'] == ename:
            for c in e['elmnt']:
                if c == "ORE":
                    print(ename, "needs", e['elmnt'][c], c)
                    if ename in e_table:
                        e_table[ename].append(cname)
                    else:
                        e_table[ename] = []
                        e_table[ename].append(cname)

                    return
                else:
                    ryield = next(k['yield'] for k in r_table if k['name'] == c)
                    print(ename, "needs", e['elmnt'][c], c, 'yields', ryield)

                    if ryield >= e['elmnt'][c]:
                        i_r = range(1)
                    else:
                        ncm = nncm(ryield, e['elmnt'][c])
                        print("NNCM", ncm, "RYIELD", ryield, "/", ncm // ryield)
                        i_r = range(ncm // ryield)

                    var_dump(i_r)
                    for i in i_r:
                        c_ore(c, e['elmnt'][c], ename)

c_ore("FUEL")
var_dump(e_table)

ore_used_total = 0
for ename, eqty in e_table.items():
    ryield = next(k['yield'] for k in r_table if k['name'] == ename)
    rore = next(k['elmnt']['ORE'] for k in r_table if k['name'] == ename)

    ncm = nncm(ryield, len(eqty))
    ore_used = int((ncm * rore) / ryield)

    ore_used_total += ore_used

    print(ename, eqty, len(eqty), ryield, "NCM:", ncm, rore, ore_used)

print(ore_used_total)
