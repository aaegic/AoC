#!/usr/bin/python3

import math

print(math.prod(sorted(list(zip(list(map(lambda x: (math.ceil((int(str(open("input.txt", mode='r').read()).strip().split("\n")[0]) / x)) * x) - int(str(open("input.txt", mode='r').read()).strip().split("\n")[0]), list(map(int, list(filter(lambda x: x != 'x', str(open("input.txt", mode='r').read()).strip().split("\n")[1].split(","))))))),list(map(int, list(filter(lambda x: x != 'x', str(open("input.txt", mode='r').read()).strip().split("\n")[1].split(",")))))))).pop(0)))

"""
   ___       __  __               _       ___
  / _ \__ __/ /_/ /  ___  ___    (_)__   / _/_ _____
 / ___/ // / __/ _ \/ _ \/ _ \  / (_-<  / _/ // / _ \
/_/   \_, /\__/_//_/\___/_//_/ /_/___/ /_/ \_,_/_//_/
     /___/
"""