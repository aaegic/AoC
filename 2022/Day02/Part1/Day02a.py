#!/usr/bin/env python

from var_dump import var_dump
from icecream import ic
import sys

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()

    itxt = [i.split() for i in itxt]
    
    #A for Rock, B for Paper, and C for Scissors.
    #X for Rock, Y for Paper, and Z for Scissors.

    hand = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
    point = { 'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3 }
    score = 0
    
    """
    score for the shape you selected
    1 for Rock, 2 for Paper, and 3 for Scissors
    plus
    0 if you lost, 3 if the round was a draw, and 6 if you won
    """
    
    for he, me in itxt:
        if point[he] == point[me]:
            #draw
            score += 3
        elif hand[he] == me:
            #win
            score += 6
            
        score += point[me]

    ic(score)
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    