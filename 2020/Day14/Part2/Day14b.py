#!/usr/bin/python3

fh = open("input.txt")
prog = fh.read().split("\n")
fh.close()

mem = dict()

for inst in prog:
    inst = list(map(lambda x: x.strip(), inst.split("=")))
    
    if inst[0][1] == 'a': #mAsk
        maskf = inst[1]
        masko = int(maskf.replace("X","0"), base=2)
        
    if inst[0][1] == 'e': #mEm
        addrb = int(inst[0][4:-1])
        opran = int(inst[1])

        xbitsi = list(map(lambda x: x[0], filter(lambda x: x[1] == "X", 
            enumerate(maskf))))
        nxbits = len(xbitsi)
        mxbits = (2 ** nxbits) - 1
        xbits = list()
        addrs = list()
        
        print("maskf", maskf)
        print("masko", bin(masko)[2:].zfill(36))
        
        addrb = list(bin(addrb)[2:].zfill(36))
        for i in xbitsi: addrb[i] = '0'
        addrb = int(str().join(addrb), base=2)
        
        for i in range(mxbits + 1):
            xbits.append(bin(i)[2:].zfill(nxbits))

        for e in xbits:
            naddr = list(maskf)
            for i in range(len(e)):
                naddr[xbitsi[i]] = e[i]
            
            addrs.append(int(str().join(naddr), base=2))

        print("addrb",bin(addrb)[2:].zfill(36))        
        for addrm in addrs:
            print("addro",bin(masko | addrb | addrm)[2:].zfill(36))
            mem.update({masko | addrb | addrm: opran})
        
print(mem)

print(sum(mem.values()))