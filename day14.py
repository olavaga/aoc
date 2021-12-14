from collections import defaultdict, Counter
from itertools import pairwise

with open('data/day14.txt', 'r') as fil:
    data = fil.read()

template= None
rules = defaultdict(str)
for line in data.splitlines():
    line = line.strip()

    if template is None:
        lastChar = line[-1]
        template = Counter(map("".join,pairwise(line)))

    elif line:
        ab, c = line.split(' -> ')
        rules[ab] = c


def pairInsertion(template):
    newTemplate = defaultdict(int)

    for ab, count in template.items():
        c = rules[ab]
        newTemplate[ab[0] + c] += count
        newTemplate[c + ab[1]] += count

    return newTemplate


for i in range(40):
    template = pairInsertion(template)

counts = {a:sum(v for k, v in template.items() if k[0]==a) for a in set("".join(template.keys()))}
counts[lastChar] += 1

result = max(counts.values()) - min(counts.values())
print(f"{result=}")
