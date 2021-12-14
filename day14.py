from collections import defaultdict, Counter
from itertools import pairwise
from functools import reduce, partial

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

def score(template, pairs):
    counts = {a:sum(v for k, v in pairs.items() if k[0]==a) 
                for a in set("".join(pairs.keys()))}
    counts[template[-1]] += 1

    return max(counts.values()) - min(counts.values())

if __name__ == '__main__':
    data = readLines('data/day14.txt')
    template = data[0]
    rules = parseDict(data, sep=' -> ')

    applyRules = partial(pairInsertion, rules=rules)
    pairs = Counter(map("".join,pairwise(template)))

    step10 = reduce(lambda a,b:b(a), [applyRules] * 10, pairs)
    step40 = reduce(lambda a,b:b(a), [applyRules] * 40, pairs)

    print(f"P1: {score(template, step10) = }")
    print(f"P2: {score(template, step40) = }")
