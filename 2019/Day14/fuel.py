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

m_table = defaultdict(int)

y_table = defaultdict(int)

fh = open("input-demo2.txt", mode='r')

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

def c_ore(ename, eqty = 1, cname = 'default'):
    global r_table
    global m_table
    global e_table
    global t_table

    tl = 0

    if ename == "FUEL":
        tl = 1

    print("====================")
    print("c_core:", ename, eqty)

    relmnts = next(k['elmnt'] for k in r_table if k['name'] == ename)

    var_dump(relmnts)

    if ename != "FUEL":
        t_table.append((ename, eqty))

    var_dump(t_table)

    for rname, rqty in relmnts.items():
        if rname == "ORE":
            print(rname, "needs", rname, eqty)
            if ename in m_table:
                m_table[ename].append(t_table)
            else:
                m_table[ename] = []
                m_table[ename].append(t_table)
        else:
            #print(ename, "needs", rname, rqty)
            #for i in range(rqty):
            c_ore(rname, rqty, ename)

        if tl == 1:
            t_table = []


            #ryield = next(k['yield'] for k in r_table if k['name'] == rname)
            #print(ename, "needs", rqty, rname, 'yields', ryield)

            #if ryield >= rqty:
            #    i_r = range(1)
            #else:
            #    ncm = nncm(ryield, rqty)
            #    print("NNCM", ncm, "RYIELD", ryield, "/", ncm // ryield)
            #    i_r = range(ncm // ryield)

            #for i in i_r:
            #    c_ore(rname, rqty, ename)

c_ore("FUEL", 1, "FUEL")

var_dump(m_table)

for i in m_table:
    print(m_table[i])


exit()
ore_used = 0
for ename, eqty in m_table.items():
    ryield = next(k['yield'] for k in r_table if k['name'] == ename)
    ore_used += nncm(ryield, sum(eqty))

print(ore_used)
















exit()
felmnts = next(k['elmnt'] for k in r_table if k['name'] == 'FUEL')
var_dump(felmnts)

ore_used = 0
ore_used_total = 0

for ename, eqty in felmnts.items():
    ore_used = 0

    ryield = next(k['yield'] for k in r_table if k['name'] == ename)
    print('FUEL', "needs", eqty, ename, 'yields', ryield)

    if ryield >= eqty:
        i_r = range(1)
    else:
        ncm = nncm(ryield, eqty)
        print("NNCM", ncm, "RYIELD", ryield, "/", ncm // ryield)
        i_r = range(ncm // ryield)

    for i in i_r:
        c_ore(ename, eqty, 'FUEL')

    var_dump(e_table)
    print(ename, "ryield:", ryield, "sum ore:", sum(e_table['ORE']),"nncm:", nncm(ryield, sum(e_table['ORE'])))
    ore_used = nncm(ryield, sum(e_table['ORE']))
    print(ore_used)

    ore_used_total += ore_used


var_dump(e_table)
print(ore_used_total)
