#!/usr/bin/env python

import sys
import numpy as np
from icecream import ic

def main () -> None:

    last = lambda in_list: in_list[len(in_list) - 1]

    itxt = open("input", mode='r').read().split()
    move = [(d, int(s)) for d, s in zip(itxt[::2], itxt[1::2])]
    dirs = {    'R': np.array([1, 0]), 'L': np.array([-1, 0]), 
                'U': np.array([0, 1]), 'D': np.array([0, -1]) }
    
    rope = [ [ np.array([0, 0]) ] for i in range(10) ]
    """
    Otherwise, if the head and tail aren't touching and aren't 
    in the same row or column, the tail always moves one step 
    diagonally to keep up:
    """
    
    def domove(i):
        if i == len(rope):
            return
        
        #ic(i)

        dif = last(rope[i-1]) - last(rope[i])
        
        if      last(rope[i-1])[0] != last(rope[i])[0] \
            and last(rope[i-1])[1] != last(rope[i])[1] \
            and (abs(dif[0]) > 1 or abs(dif[1]) > 1):
            #ic('diag', i, )
            if dif[0] > 0 and dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([1,1]))
            elif dif[0] > 0 and dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([1,-1]))
            elif dif[0] < 0 and dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([-1,1]))
            elif dif[0] < 0 and dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([-1,-1]))
        
        elif abs(dif[0]) > 1 or abs(dif[1]) > 1:
            #ic('notouch', d, i, last(rope[i]), dirs.get(d), last(rope[i]) + dirs.get(d))
            #rope[i].append(rope[i-1][-2])
            #rope[i].append(last(rope[i]) + dirs.get(d))
            
            if dif[0] > 0:
                rope[i].append(last(rope[i]) + np.array([1,0]))
            elif dif[0] < 0:
                rope[i].append(last(rope[i]) + np.array([-1,0]))
            elif dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([0,1]))
            elif dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([0,-1]))
        
        #draw(rope)
        
        domove(i+1)
        
    
    for d, s in move:
        #ic(d,s)
        for _ in range(s):
            rope[0].append(last(rope[0]) + dirs.get(d))
            
            domove(1)
        #draw(rope)
    
    print(len(set([ (i[0], i[1]) for i in rope[-1]])))

def draw(rope):
    last = lambda in_list: in_list[len(in_list) - 1]
    print('   ', end='')
    for i in range(-15,15,1):
        if i > 9 or i < 0:
            x = str(i)[1]
        else:
            x = str(i)[0]
            
        print(x, end='')
    print("\n", end='')
    
    for y in range(15,-7,-1):
        
        if y > 9 or y < 0:
            ny = str(y)[1]
        else:
            ny = str(y)[0]
        
        print(ny, ' ', end='')
        
        for x in range(-15,15,1):
            if x == 0 and y == 0:
                print('s',end='')
                continue
                
            xx=[ (i[0], i[1]) for i in rope[-1]]
            if  (x,y) in xx:
                print('#',end='')
                continue
            
            loc = np.array([x,y])
            found = False
            for i, knot in enumerate(rope):
                if loc[0] == last(knot)[0] and loc[1] == last(knot)[1]:
                    print(i,end='')
                    found = True
                    break
            
            if found == False:
                print('.', end='')
                
        print("\n", end='')
            

    
    
if __name__ == '__main__':
    sys.exit(main()) 
    
    