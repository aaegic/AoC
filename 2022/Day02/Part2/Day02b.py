#!/usr/bin/env python

from var_dump import var_dump
from icecream import ic
import sys

def main () -> int:

    itxt = open("input", mode='r').read().splitlines()

    itxt = [i.split() for i in itxt]
    
    """
    A for Rock, B for Paper, and C for Scissors.
    X means you need to lose,
    Y means you need to draw,
    Z means you need to win.
    """

    hands = {   'X': { 'A': 'C', 'B': 'A', 'C': 'B' },  #lose
                'Y': { 'A': 'A', 'B': 'B', 'C': 'C' },  #draw
                'Z': { 'A': 'B', 'B': 'C', 'C': 'A' } } #win
    
    """
    score for the shape you selected
    1 for Rock, 2 for Paper, and 3 for Scissors
    plus
    0 if you lost, 3 if the round was a draw, and 6 if you won
    """

    point = { 'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3 }
    
    ic(sum([point[do] + point[hands[do][he]] for he, do in itxt]))
    

if __name__ == '__main__':
    sys.exit(main()) 
    
    