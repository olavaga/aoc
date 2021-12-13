from aocd import submit, data

points = []
folds = []
fold_section = False
for line in data.splitlines():
    if not line:
        fold_section = True
        continue

    if fold_section:
        text, dist = line.strip().split('=')
        folds.append(('x' in text, int(dist)))
    
    else:
        points.append(tuple(map(int,line.strip().split(','))))

p1 = None
for isHorizontal, line in folds:
    if isHorizontal:
        points = [*map(lambda p:(line * 2 - p[0] if p[0] > line else p[0],p[1]), points)]
    else:
        points = [*map(lambda p:(p[0], line * 2 - p[1] if p[1] > line else p[1]), points)]

    if p1 is None:
        p1 = len(set(points))

print("Part one", p1)

print("Part two")
for i in range(8):
    s = ""
    for j in range(50):
        if (j,i) in points:
            s += '#'
        else:
            s += '.'
    print(s)

