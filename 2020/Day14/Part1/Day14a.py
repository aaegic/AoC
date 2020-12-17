#!/usr/bin/python3

fh = open("input.txt")
prog = fh.read().split("\n")
fh.close()

mask = ""
mem = dict()

for inst in prog:
    inst = list(map(lambda x: x.strip(), inst.split("=")))
    
    if inst[0][1] == 'a': #mAsk
        mask1 = inst[1].replace('X', '1')
        mask1 = int(mask1, base=2)
        mask2 = inst[1].replace('X', '0')
        mask2 = int(mask2, base=2)        
        
    if inst[0][1] == 'e': #mEm
        addr = int(inst[0][4:-1])
        opra = mask2 | mask1 & int(inst[1])
        mem.update({addr:  opra})
        
print(mem)

print(sum(mem.values()))
        
