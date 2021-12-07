#!/usr/bin/env python

itxt = open("input-test", mode='r').read().strip().splitlines()
fish = list(map(int, itxt[0].split(',')))

for i in range(80):
    fish = [fish[j] - 1 for j in range(len(fish))] #decrement fish
    fish += [8] * fish.count(-1) #spawn fish
    fish = [6 if j == -1 else j for j in fish] #reset fish

print(len(fish))