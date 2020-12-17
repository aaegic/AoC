#!/usr/bin/python3

fh = open("input-test2.txt")
prog = fh.read().split("\n")
fh.close()

mask = ""
mem = dict()

for inst in prog:
    inst = list(map(lambda x: x.strip(), inst.split("=")))
    
    if inst[0][1] == 'a': #mAsk
        mask = inst[1]
        xbitsi = list(map(lambda x: x[0], filter(lambda x: x[1] == "X", 
            enumerate(mask))))
        nxbits = len(xbitsi)
        mxbits = (2 ** nxbits) - 1
        xbits = list()
        addrs = list()
                
        for i in range(mxbits + 1):
            xbits.append(bin(i)[2:].zfill(nxbits))

        for e in xbits:
            naddr = list(mask)
            for i in range(len(e)):
                naddr[xbitsi[i]] = e[i]
            
            print(str().join(naddr))
            addrs.append(int(str().join(naddr), base=2))

        print(addrs)

        print(xbitsi, mxbits, xbits)
        
    if inst[0][1] == 'e': #mEm
        addr = int(inst[0][4:-1])
        opra = int(inst[1])
        mem.update({addr:  opra})
        
        for addr in addrs:
            mem.update({addr: opra})
        
print(mem)

#print(sum(mem.values()))
        
