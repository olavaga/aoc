from aocd import data
from dataclasses import dataclass

@dataclass
class Cube:
    x : int
    y : int
    z : int

    w : int
    h : int
    b : int

    on : bool

    def volume(self):
        return self.w * self.h * self.b

    def end(self):
        return (self.x+self.w, self.y+self.h, self.z+self.b)

    def intersection(self, other):
        x = max(self.x, other.x)
        y = max(self.y, other.y)
        z = max(self.z, other.z)

        x1, y1, z1 = self.end()
        x2, y2, z2 = other.end()
        
        c = Cube(x, y, z, min(x1,x2) - x, min(y1,y2) - y, min(z1,z2) - z, other.on)
        
        if c.volume() > 0:
            return c

        else:
            return Cube(0,0,0,0,0,0,other.on)

def parseCube(line):
    state, cuboid = line.split()
    x,y,z = cuboid.split(',')
    _,x = x.split('=')
    _,y = y.split('=')
    _,z = z.split('=')
    x = [*map(int,x.split('..'))]
    y = [*map(int,y.split('..'))]
    z = [*map(int,z.split('..'))]
    c = Cube(x[0], y[0], z[0], x[1]-x[0], y[1]-y[0], z[1]-z[0], state == 'on')
    return c

def readData(data):
    return [parseCube(l) for l in data.splitlines()]
    
def constrainedBruteForce(cuboids):
    cubes = set()

    for c in cuboids:
        def cuboid():
            r = lambda t: range(max(t[0],-50), min(t[1]+1,50))
            for i in r((c.x, c.x+c.w)):
                for j in r((c.y, c.y+c.h)):
                    for k in r((c.z, c.z+c.b)):
                        yield i,j,k

        if c.on:
            for x1,y1,z1 in cuboid():
                cubes.add((x1,y1,z1))
        else:
            for p in cuboid():
                cubes.discard(p)

    return len(cubes)

def calcOn(cuboids):
    on = []
    off = []
    points = 0

    for new_cube in cuboids:
        offs = []
        for on_cube in on:
            overlap_cube = on_cube.intersection(new_cube)
            if new_cube.on:
                points -= overlap_cube.volume()
            offs.append(overlap_cube)

        ons = []
        for off_cube in off:
            overlap_cube = off_cube.intersection(new_cube)
            if not new_cube.on:
                points += overlap_cube.volume()
            ons.append(overlap_cube)

        points += sum(c.volume() for c in ons)
        points -= sum(c.volume() for c in offs)
        on += ons
        off += offs

        if new_cube.on:
            points += new_cube.volume()
            on.append(new_cube)
        else:
            off.append(new_cube)

    return points

def countIntersections(cuboids):
    intersections = 0

    for i, c in enumerate(cuboids):
        for d in cuboids[:i]:
            ints = c.intersection(d)
            if ints.volume():
                intersections += 1

    return intersections


if __name__ == '__main__':
    cuboids = readData(data)
    print(f"{countIntersections(cuboids)=}")
    print("P1",constrainedBruteForce(cuboids))
    print("P2",calcOn(cuboids))
    
