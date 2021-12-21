from aocd import data
from dataclasses import dataclass
from collections import Counter
from itertools import permutations, combinations

@dataclass
class Scanner:
    sid : int
    beacons : set

def initializeScanners(data):
    scanners = []
    sid = 0
    beacons = set()
    for l in data.splitlines():
        if not l:
            scanners.append(Scanner(sid, beacons))
            sid = 0
            beacons = set()
        elif 'scanner' in l:
            sid = int(l.split()[2])
        else:
            beacons.add(tuple(map(int,l.split(','))))
    if beacons:
        scanners.append(Scanner(sid, beacons))
    return scanners

def composite_function(f, g):
    return lambda x: f(g(x))

def orientations():
    # Facing any of +x/-x (x,y,z) and considering any of 4 dirs up
    rotate = lambda t: (t[0],t[2],-t[1])
    face = lambda t: (t[1],t[2],t[0])
    inverse = lambda t: (-t[0],-t[1],t[2])

    f = lambda t:t
   
    for _ in range(3):
        for _ in range(4):
            yield f
            yield composite_function(inverse,f)
            f = composite_function(rotate,f)
        f = composite_function(face,f)

def matches(sc1, sc2):
    for facing in orientations():
        for x1, y1, z1 in sc1.beacons:
            for x2, y2, z2 in map(facing,sc2.beacons):
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2

                m = sum((x + dx, y + dy, z + dz) in sc1.beacons 
                        for x,y,z in map(facing,sc2.beacons))

                if m >= 12:
                    return (facing, dx,dy,dz)

    return False

def composite(sc):
    comp = sc[0]
    comp.scanners = [(0,0,0)]
    insert = sc[1:]

    while insert:
        n = []
        for s in insert:
            if r:=matches(comp, s):
                f, dx, dy, dz = r
                trans=map(lambda t:(t[0]+dx,t[1]+dy,t[2]+dz),map(f,s.beacons))
                comp.beacons.update(set(trans))
                comp.scanners.append((dx,dy,dz))
            else:
                n.append(s)
        insert = n

    return comp

def largest_distance(scanners):
    manhattan = lambda ps: sum(abs(a-b) for a,b in zip(*ps))
    return max(map(manhattan,combinations(scanners,2)))

if __name__ == '__main__':
    sc = initializeScanners(data)
    s = composite(sc)

    print("P1",len(s.beacons))
    print("P2",largest_distance(s.scanners))
