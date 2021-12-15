from aocd import data, submit
from heapq import heappush, heappop

def djikstra(matrix):
    dists = [[2**64] * len(matrix[0]) for _ in matrix]

    dists[0][0] = 0
    kø = [(0,0,0)]
    seen = set([(0,0)])

    while not (len(matrix[0]) - 1, len(matrix) - 1) in seen:
        d,x,y = heappop(kø)
        for s,t in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (s,t) in seen:
                continue
            if 0 <= s < len(matrix[0]) and 0 <= t < len(matrix):
                dists[s][t] = min(dists[s][t], dists[x][y] + matrix[s][t])
                heappush(kø, (dists[s][t],s,t))
                seen.add((s,t))

    return dists[-1][-1]

if __name__ == '__main__':
    matrix = [tuple(map(int, line.strip())) for line in data.splitlines()]
    print(djikstra(matrix))

    large = matrix.copy()
    for i in range(1, 5):
        for j, row in enumerate(large):
            large[j] = row + tuple((n + i) % 10 + (n + i) // 10 for n in matrix[j])

    larger = large.copy()
    for i in range(1, 5):
        larger += [[(n + i) % 10 + (n + i) // 10 for n in row] for row in large]

    print(djikstra(larger))

