#!/usr/bin/python3

def xtend(f):
    def wrap(self, index, *args):
        if len(self) <= index:
            self.extend([self._gen()] * (index - len(self) + 1))
        return f(self, index, *args)
    return wrap

class defaultlist(list):
    def __init__(self, gen, lst = []):
        list.__init__(self, lst)
        self._gen = gen

    __setitem__ = xtend(list.__setitem__)
    __getitem__ = xtend(list.__getitem__)

ic = defaultlist(int, [3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0])

def intcode(intc_inbuf, ic):

    _ptr = 0
    _rel = 0

    robo_inbuf = []
    robo_f = 90

    plane = [{
        'x': 0,
        'y': 0,
        'c': 0
    }]

    def get_opand(g_opand):
        if g_opand == 0:
            if _pm0 == 2:
                #   2 = relative mode
                return ic[ic[_ptr+1] + _rel]
            elif _pm0 == 1:
                #   1 = immediate mode
                return ic[_ptr+1]
            else:
                #   0 = position mode
                return ic[ic[_ptr+1]]
        elif g_opand == 1:
            if _pm1 == 2:
                return ic[ic[_ptr+2] + _rel]
            elif _pm1 == 1:
                return ic[_ptr+2]
            else:
                return ic[ic[_ptr+2]]
        elif g_opand == 2:
            if _pm2 == 2:
                return ic[_ptr+3] + _rel
            elif _pm1 == 1:
                return ic[_ptr+3]
            else:
                return ic[_ptr+3]

    def robo_go(inbuf=-1):
        nonlocal robo_f

        if inbuf == -1: 
            for i in range(len(plane)-2, -1, -1):
                if plane[i]['x'] == plane[-1]['x'] and plane[i]['y'] == plane[-1]['y']:
                    return plane[i]['c']
            return(1)

        robo_inbuf.append(inbuf)

        if len(robo_inbuf) < 2: return

        plane[-1]['c'] = robo_inbuf.pop(0)

        _dir = robo_inbuf.pop(0)

        if _dir == 0:
            robo_f = robo_f - 90
        elif _dir == 1:
            robo_f = robo_f + 90

        if robo_f >= 360:
            robo_f = 0
        elif robo_f < 0:
            robo_f = 270

        # 0 left
        # 90 up
        # 180 right
        # 270 down

        if robo_f == 0:
            plane.append({'x': plane[-1]['x'] - 1, 
            'y': plane[-1]['y'], 
            'c': 0
            })
        elif robo_f == 90:
            plane.append({'x': plane[-1]['x'],
            'y': plane[-1]['y'] - 1, 
            'c': 0
            })
        elif robo_f == 180:
            plane.append({'x': plane[-1]['x'] + 1,
            'y': plane[-1]['y'], 
            'c': 0
            })
        elif robo_f == 270:
            plane.append({'x': plane[-1]['x'], 
            'y': plane[-1]['y'] + 1, 
            'c': 0
            })
        
        return


    while True:
        _oc = ic[_ptr] % 100

        _pm2 = (ic[_ptr] / 10000).__trunc__() % 10
        _pm1 = (ic[_ptr] / 1000).__trunc__() % 10
        _pm0 = (ic[_ptr] / 100).__trunc__() % 10

        #   Addition
        if _oc == 1:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)
            __opand2 = get_opand(2)

            ic[__opand2] = __opand0 + __opand1
            _ptr += 4

        #   Multiplication
        if _oc == 2:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)
            __opand2 = get_opand(2)

            ic[__opand2] = __opand0 * __opand1
            _ptr += 4

        #   Input
        if _oc == 3:
            ic[ic[_ptr+1] + _rel] = robo_go()
            _ptr += 2

        #   Output
        if _oc == 4:
            __opand0 = get_opand(0)

            robo_go(__opand0)
            _ptr += 2

        #   jump-if-true
        if _oc == 5:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)

            if __opand0:
                _ptr = __opand1
            else:
                _ptr += 3

        #   jump-if-false
        if _oc == 6:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)

            if not __opand0:
                _ptr = __opand1
            else:
                _ptr += 3

        #   less than
        if _oc == 7:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)
            __opand2 = get_opand(2)

            if __opand0 < __opand1:
                ic[__opand2] = 1
            else:
                ic[__opand2] = 0

            _ptr += 4

        #   equals
        if _oc == 8:
            __opand0 = get_opand(0)
            __opand1 = get_opand(1)
            __opand2 = get_opand(2)

            if __opand0 == __opand1:
                ic[__opand2] = 1
            else:
                ic[__opand2] = 0

            _ptr += 4

        #   adjust relative base
        if _oc == 9:
            __opand0 = get_opand(0)

            _rel = _rel + __opand0
            _ptr += 2

        #   halt
        if _oc == 99:
            return plane


def getpcol(x, y):
    for i in range(len(plane)-1, -1, -1):
        if plane[i]['x'] == x and plane[i]['y'] == y:
            return plane[i]['c']


""" Part 1, sort and look for duplicates """

plane = intcode([0], ic)
plane.sort(key=lambda i: (i['x'], i['y']))

j = 0
for i in range(len(plane)):
    k = 1
    if plane[i]['x'] == plane[i-1]['x'] and plane[i]['y'] == plane[i-1]['y']:
        k = 0

    j = j + k


""" Part 2, output image """

"""the robot was expecting to start on a white panel, not a black one. """
""" XXX change line 78 to return(1) XXX """

for y in range(6):
    for x in range(41):
        _c = getpcol(x, y)
        if _c == 1:
            print("▓", end="")
        else:
            print("░", end="")

    print()

"""
░▓░░▓░▓░░░░░▓▓░░▓▓▓▓░░▓▓░░▓▓▓▓░░▓▓░░▓░░▓░
░▓░▓░░▓░░░░▓░░▓░░░░▓░▓░░▓░▓░░░░▓░░▓░▓░░▓░
░▓▓░░░▓░░░░▓░░░░░░▓░░▓░░▓░▓▓▓░░▓░░░░▓░░▓░
░▓░▓░░▓░░░░▓░░░░░▓░░░▓▓▓▓░▓░░░░▓░▓▓░▓░░▓░
░▓░▓░░▓░░░░▓░░▓░▓░░░░▓░░▓░▓░░░░▓░░▓░▓░░▓░
░▓░░▓░▓▓▓▓░░▓▓░░▓▓▓▓░▓░░▓░▓▓▓▓░░▓▓▓░░▓▓░░
"""