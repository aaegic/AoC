#!/usr/bin/env python

import sys
from icecream import ic
from var_dump import var_dump
import math as math

def main () -> int:
    class pheader:
        def __init__(self, ver, typ) -> None:
            self.ver = ver
            self.typ = typ
        def opr(self, opr) -> None:
            self.opr = opr
        def lng(self, lng) -> None:
            self.lng = lng
        
    class packet:
        def __init__(self, header, data) -> None:
            self.header = header
            self.data = data
    
    def parse(P,B,S=False):
        def get(n: int) -> str:
            nonlocal ptr
            ptr += n
            return(B[ptr-n:ptr])

        def literal():
            data = str()
            while int(get(1),2) != 0:
                data += get(4) 
            else:
                data += get(4)
                data = int(data,2)
            return data

        def oper():
            nonlocal ptr
            data = list()
            header.opr(int(get(1),2))
            if header.opr == 0:
                header.lng(int(get(15),2))

                NP, NB = 0, get(header.lng)

                while NP < header.lng:
                    (NP, d) = parse(NP, NB, True)
                    data.append(d)

            elif header.opr == 1:
                header.lng(int(get(11),2))
            
                NP, NB = ptr, B 

                for _ in range(header.lng):
                    (NP, d) = parse(NP, NB, True)
                    data.append(d)

                ptr = NP

            return data

        ops = dict({0: 'sum', 1: 'prod', 2: 'min', 3: 'max', 4: 'lit', 5: 'gt', 6: 'lt', 7: 'eq'})

        ptr = P
        data = str()
        nonlocal STACK

        header = pheader(int(get(3),2),int(get(3),2))
        

        if header.typ == 4:
            rdata = list()
            rdata.append(literal())
            ic(rdata)
        else:
            data = oper()
            print(ops[header.typ])
            match header.typ:
                case 0: 
                    STACK = [sum(STACK)]
                case 1:
                    STACK = [math.prod(STACK)]
                case 2: 
                    STACK = [min(STACK)]
                case 3: 
                    STACK = [max(STACK)]
                case 5:
                    if STACK[-1] > STACK[-2]:
                        STACK = [1]
                    else:
                        STACK = [0]
                case 6:
                    if STACK[-1] < STACK[-2]:
                        STACK = [1]
                    else:
                        STACK = [0]
                case 7:
                    if STACK[-1] == STACK[-2]:
                        STACK = [1]
                    else:
                        STACK = [0]

        if S == False:
            ptr = -(ptr//-8)*8

        return((ptr, packet(header, data)))

    """
  .-""-.
 /,..___\
() {_____}
  (/-@-@-\)
  {`-=^=-'}
  {  `-'  } HoHoHo
   {     }
    `---'
    """

    P = 0
    B = str()
    STACK = list()

    for i in "9C0141080250320F1802104A08": #"9C0141080250320F1802104A089C0141080250320F1802104A08": #"880086C3E88112": #"04005AC33890": #"C200B40A82":# "04005AC33890": #open("input", mode='r').readline(): 
        B += bin(int(i,16))[2:].zfill(4)

    while P < len(B):
        (P, buf) = parse(P,B)

    ic(STACK)
    
if __name__ == '__main__':
    sys.exit(main()) 