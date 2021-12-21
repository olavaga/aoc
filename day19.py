from aocd import data
from dataclasses import dataclass
from collections import Counter
from itertools import permutations, combinations

@dataclass
class Scanner:
    sid : int
    beacons : set

def composite_function(f, g):
    return lambda x: f(g(x))

def orientations():
    # Facing any of +x/-x (x,y,z) and considering any of 4 dirs up
    rotate = lambda t: (t[0],t[2],-t[1])
    face = lambda t: (t[1],t[2],t[0])
    inverse = lambda t: (-t[0],-t[1],t[2])

    f = lambda t:t
    i = inverse
   
    for _ in range(4):
        yield f
        yield i
        f = composite_function(rotate,f)
        i = composite_function(rotate,i)

    f = face
    i = composite_function(f, i)

    for _ in range(4):
        yield f
        yield i
        f = composite_function(rotate,f)
        i = composite_function(rotate,i)

    f = composite_function(face, face)
    i = composite_function(f, i)

    for _ in range(4):
        yield f
        yield i
        f = composite_function(rotate,f)
        i = composite_function(rotate,i)


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

def matches(sc1, sc2):
    
    for facing in orientations():
        for x1, y1, z1 in sc1.beacons:
            for x2, y2, z2 in map(facing,sc2.beacons):
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2

                m = sum((x + dx, y + dy, z + dz) in sc1.beacons 
                        for x,y,z in map(facing,sc2.beacons))

                if m >= 12:
                    return facing, (dx,dy,dz)

    return False

def composite(sc):
    while len(sc) > 1:
        joined = dict()
        print("Current sc-size", len(sc))
        print("Current ids", *(s.sid for s in sc))
        seen = set()
        for s1, s2 in permutations(sc, 2):
            if s1.sid in seen or s2.sid in seen:
                continue

            if r:=matches(s1, s2):
                print(f"Match {s1.sid=} - {s2.sid=}")
                f, dist = r
                dx, dy, dz = dist
                print(f"Data {r=}")
                trans=map(lambda t:(t[0]+dx,t[1]+dy,t[2]+dz),map(f,s2.beacons))
                ns = Scanner(s1.sid, s1.beacons.union(set(trans)))
                print(f"{len(s1.beacons)} + {len(s2.beacons)} = {len(ns.beacons)}")
                joined[tuple(sorted([s1.sid,s2.sid]))] = ns
                seen.add(s1.sid)
                seen.add(s2.sid)
        sc = [s for s in sc if not s.sid in seen]
        sc += [*joined.values()]

    return max(sc, key=lambda s: len(s.beacons))

def largest_distance(s):
    manhattan = lambda p,q: sum(abs(a-b) for a,b in zip(p,q))
    largest = 0

    for a,b in combinations(s.beacons, 2):
        if manhattan(a,b) > largest:
            print('largest','\n',a,'\n',b)
            largest = manhattan(a,b)

    return largest

if __name__ == '__main__':
    sc = initializeScanners(data)
    print(len(sc))
    print(set(len(s.beacons) for s in sc))

    s = composite(sc)
    print(len(s.beacons))
