from collections import defaultdict, Counter
from itertools import pairwise

def readLines(filnavn):
    with open(filnavn, 'r') as fil:
        data = fil.read().splitlines()
    return [*map(str.strip, data)]

def parseDict(data, sep):
    return dict(line.split(sep) for line in data if sep in line)

def pairInsertion(pairs, rules):
    newPairs = defaultdict(int)

    for ab, count in pairs.items():
        c = rules[ab]
        newPairs[ab[0] + c] += count
        newPairs[c + ab[1]] += count

    return newPairs

def compute(steps, pairs, rules, lastChar):
    for i in range(steps):
        pairs = pairInsertion(pairs, rules)

    counts = {a:sum(v for k, v in pairs.items() if k[0]==a) for a in set("".join(pairs.keys()))}
    counts[lastChar] += 1

    return max(counts.values()) - min(counts.values())

if __name__ == '__main__':
    data = readLines('data/day14.txt')
    template = data[0]
    rules = parseDict(data, sep=' -> ')

    pairs = Counter(map("".join,pairwise(template)))
    lastChar = data[0][-1]

    print(f"P1: {compute(10, pairs, rules, lastChar) = }")
    print(f"P2: {compute(40, pairs, rules, lastChar) = }")
