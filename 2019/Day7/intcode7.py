#!/usr/bin/python3


import itertools as it
from var_dump import var_dump


def intcode(input, ic):

    _ptr = 0
    output = []

    while True:
        _oc = ic[_ptr] % 100

        _pm2 = (ic[_ptr] / 10000).__trunc__() % 10
        _pm1 = (ic[_ptr] / 1000).__trunc__() % 10
        _pm0 = (ic[_ptr] / 100).__trunc__() % 10

        #   Addition
        if _oc == 1:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            ic[ic[_ptr+3]] = __opand0 + __opand1
            _ptr += 4

        #   Multiplication
        if _oc == 2:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            ic[ic[_ptr+3]] = __opand0 * __opand1
            _ptr += 4

        #   Input
        if _oc == 3:
            ic[ic[_ptr+1]] = input.pop(0)
            _ptr += 2

        #   Output
        if _oc == 4:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            output.append(__opand0)
            _ptr += 2

        #   jump-if-true
        if _oc == 5:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            if __opand0:
                _ptr = __opand1
            else:
                _ptr += 3

        #   jump-if-false
        if _oc == 6:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            if not __opand0:
                _ptr = __opand1
            else:
                _ptr += 3

        #   less than
        if _oc == 7:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            if __opand0 < __opand1:
                ic[ic[_ptr+3]] = 1
            else:
                ic[ic[_ptr+3]] = 0

            _ptr += 4

        #   equals
        if _oc == 8:
            if _pm0:
                __opand0 = ic[_ptr+1]
            else:
                __opand0 = ic[ic[_ptr+1]]

            if _pm1:
                __opand1 = ic[_ptr+2]
            else:
                __opand1 = ic[ic[_ptr+2]]

            if __opand0 == __opand1:
                ic[ic[_ptr+3]] = 1
            else:
                ic[ic[_ptr+3]] = 0

            _ptr += 4

        #   halt
        if _oc == 99:
            return output


ic = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

"""
ic = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

ic = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1,
    23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]

ic = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
    1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
"""

digits = [ 0, 1, 2, 3, 4 ]
permut = list(it.permutations(digits))

#permut = []
#permut.append([1,0,4,3,2])

thrust = 0
for i in permut:
    input = 0
    for j in i:
        ic_i = ic
        input = intcode([j, input], ic_i)
        input = int(input[0])

        if input > thrust:
            thrust = input

print(thrust)
