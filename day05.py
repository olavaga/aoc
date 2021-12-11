from itertools import zip_longest

# Parse inputs
lines = []
with open('data/day5.txt', 'r') as fil:
    for line in fil.read().splitlines():
        a,b = line.split(' -> ')
        a = tuple(map(int,a.split(',')))
        b = tuple(map(int,b.split(',')))
        
        lines.append((a,b))

# Keep track of all seen points, repeats are added to crosses
seen = set()
crosses = set()

for a,b in lines:
    # Account for stepping towards smaller numbers
    dirx = 1 if b[0] > a[0] else -1
    diry = 1 if b[1] > a[1] else -1

    xs = range(a[0], b[0] + dirx, dirx)
    ys = range(a[1], b[1] + diry, diry)

    # Repeat single value when start is equal to end (horisontal/vertical)
    default = a[0] if a[0] == b[0] else a[1]

    points = set(zip_longest(xs, ys, fillvalue=default))

    crosses |= seen & points
    seen |= points

# Output the count
print(len(crosses))
