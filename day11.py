from aocd import data, submit

octopuses = [[*map(int,l.strip())] for l in data.splitlines()]
flat = lambda m: [it for r in m for it in r]

def flash(m, p):
    x, y = p
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < 10 and 0 <= y + j < 10:
                m[x + i][y + j] += 1

flashes = 0
allFlashed = 0
step = 0
while True:
    octopuses =[[n+1 for n in l] for l in octopuses]
    hasFlashed = [[False]*10 for _ in range(10)]

    while any(o > 9 and not flashed for o, flashed in zip(flat(octopuses),flat(hasFlashed))):
        

        for i, l in enumerate(octopuses):
            for j, oc in enumerate(l):
                if oc > 9 and not hasFlashed[i][j]:
                    flash(octopuses, (i,j))
                    hasFlashed[i][j] = True
    step += 1

    if step < 100:
        flashes += sum(flat(hasFlashed))

    if not allFlashed and all(flat(hasFlashed)):
        allFlashed = step

    if step >= 100 and allFlashed:
        break

    for i, l in enumerate(octopuses):
        for j, oc in enumerate(l):
            if hasFlashed[i][j]:
                octopuses[i][j] = 0

submit(allFlashed)
