#!/usr/bin/env python

import sys

def main () -> None:

    class monkey:        
        def __init__(self, attrs: dict):
            self.attrs = attrs
            self.items_inspected = 0
        
        def throw (self):
            items = list()
            
            for old in self.attrs['items']:
                self.items_inspected += 1
                old = eval(self.attrs['operation']) // 3
                
                if old % self.attrs['test'] == 0:
                    items.append((self.attrs['true'], old))
                else:
                    items.append((self.attrs['false'], old))
            
            self.attrs['items'].clear()
            return items
            
        def catch (self, item):
            self.attrs['items'].append(item)

            
    itxt = open("input-test", mode='r').read().split("\n\n")
    itxt = [i.split("\n") for i in itxt]
    
    monkeys = list()

    for m in itxt:
        monkeys.append(monkey({
                'items': [int(i) for i in  m[1][17:].split(",")],
                'operation': m[2][19:], 'test': int(m[3][20:]),
                'true': int(m[4][-1]), 'false': int(m[5][-1])
            }))
        
    for _ in range(20):
        for m in monkeys:
            for md, item in m.throw():
                monkeys[md].catch(item)

    active = sorted([m.items_inspected for m in monkeys])
    print(active[-2] * active[-1])

    
if __name__ == '__main__':
    sys.exit(main()) 
    