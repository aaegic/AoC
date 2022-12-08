#!/usr/bin/env python

import sys

def main () -> None:

    itxt = open("input", mode='r').read().splitlines()
    tree = {(x,y): t for y, row in enumerate(itxt) for x, t in enumerate(list(row))}
    visi = {(x,y): 0 for y, row in enumerate(itxt) for x, _ in enumerate(list(row))}

    for xt, yt in tree.keys():
        if xt == 0 or yt == 0 or xt == len(list(itxt)) or yt == len(itxt):
            continue
        
        lr = rl = tb = bt = 0
        
        for xc in range(xt + 1, len(list(itxt))): #l->r
            lr += 1
            
            if tree.get((xc,yt)) >= tree.get((xt,yt)):
                break

        for xc in range(xt - 1, -1, -1): #r->l
            rl += 1
            
            if tree.get((xc,yt)) >= tree.get((xt,yt)):
                break

        for yc in range(yt + 1, len(itxt)): #t->b
            tb += 1
            
            if tree.get((xt,yc)) >= tree.get((xt,yt)):
                break
            
        for yc in range(yt - 1, -1, -1): #b->t
            bt += 1
            
            if tree.get((xt,yc)) >= tree.get((xt,yt)):
                break

        visi.update({ (xt,yt): lr * rl * tb * bt })

    print(sorted(visi.values())[-1])


if __name__ == '__main__':
    sys.exit(main()) 
    
    