from itertools import zip_longest

# Parse inputs
lines = []
with open('day5.txt', 'r') as fil:
    for line in fil.read().splitlines():
        a,b = line.split(' -> ')
        a = tuple(map(int,a.split(',')))
        b = tuple(map(int,b.split(',')))
        
        lines.append((a,b))

# Create and plot chart
chart = [[0] * 1000 for _ in range(1000)]

for a,b in lines:
    dirx = 1 if b[0] > a[0] else -1
    diry = 1 if b[1] > a[1] else -1

    xs = range(a[0], b[0] + dirx, dirx)
    ys = range(a[1], b[1] + diry, diry)

    default = a[0] if a[0] == b[0] else a[1]

    for x,y in zip_longest(xs, ys, fillvalue=default):
        chart[x][y] += 1

# Count intersections and output
print(sum(n > 1 for line in chart for n in line))
