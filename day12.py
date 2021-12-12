from aocd import data, submit
from collections import defaultdict

caveMap = defaultdict(set)

for edge in data.splitlines():
    start, end = edge.strip().split('-')
    caveMap[start].add(end)
    caveMap[end].add(start)

def DFS(path : tuple, twiceSmall : bool = False) -> int:
    if 'end' == path[-1]:
        return 1
    paths = 0
    
    for neighbour in caveMap[path[-1]]:
        if neighbour == 'start':
            continue

        elif neighbour.isupper() or not neighbour in path:
            paths += DFS(path + (neighbour,), twiceSmall)

        elif not twiceSmall:
            paths += DFS(path + (neighbour,), True)

    return paths

print('P1',DFS(('start',), True))
print('P2',DFS(('start',)))
