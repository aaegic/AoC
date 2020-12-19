#!/usr/bin/python3

ipt = [ 0,3,6 ]
ipt = [ 3,1,2 ]
ipt = [ 1,2,3 ]
ipt = [ 8,11,0,19,1,2 ]

for i in range(len(ipt)-1, 2019):
    if ipt[i] not in ipt[0:i]:
        ipt.append(0)
    else:
        rpt = list(reversed(ipt))
        pi = len(ipt) - rpt.index(ipt[i],1)
        d = (i+1) - pi
        ipt.append(d)
    
    print(i+2, ipt[-20:])
    