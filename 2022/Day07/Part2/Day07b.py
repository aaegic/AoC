#!/usr/bin/env python

import sys
import re

def main () -> int:

    itxt = open("input", mode='r').read()
    itxt = itxt.splitlines()
    
    path = list()
    tree = dict()
    
    for l in itxt:
        if l == '$ cd ..':
            path.pop(-1)
            continue
        
        if l.startswith('$ cd'):
            path.append(l[5:])
            
            if '/'.join(path) not in tree.keys():
                tree.update({ '/'.join(path): 0 })
            
            continue
        
        if re.search("^\d+ ", l):
            size, _ = l.split(' ')
            pwd = list()
            
            for d in path:
                pwd.append(d)
                tree.update({ '/'.join(pwd): tree['/'.join(pwd)] + int(size) })
                
            continue

    for i in sorted(tree.values()):
        if i > 30000000 - (70000000 - tree['/']):
            print(i)
            return
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    