from aocd import data
from collections import Counter, namedtuple, defaultdict
from itertools import product

def getData():
    lines = data.splitlines()
    p1 = lines[0].split()[-1]
    p2 = lines[1].split()[-1]

    return int(p1), int(p2)

score1 = score2 = 0
p1, p2 = getData()

def roll():
    ddice = 1
    while True:
        r = ddice
        ddice = (ddice + 1) % 100 or 100
        r += ddice
        ddice = (ddice + 1) % 100 or 100
        r += ddice
        ddice = (ddice + 1) % 100 or 100
        yield r

rolls = 0
dice = iter(roll())
while score1 < 1000 and score2 < 1000:
    p1 = (p1 + next(dice)) % 10 or 10
    rolls += 3
    score1 += p1

    if score1 > 999 or score2 > 999:break

    p2 = (p2 + next(dice)) % 10 or 10
    rolls += 3
    score2 += p2

print(f"P1 {min(score1, score2) * rolls = }")

qdice = Counter(sum(t) for t in product([1,2,3], repeat=3))
state = namedtuple('state', ['p1','score1','p2','score2'])

p1, p2 = getData()
futures = {state(p1, 0, p2, 0):1}
p1_wins = 0
p2_wins = 0

while futures:
    new_futures = defaultdict(int)

    for f, ps in futures.items():
        for roll, ns in qdice.items():
            p1 = (f.p1 + roll) % 10 or 10
            if 21 <= f.score1 + p1:
                p1_wins += ns * ps
                continue

            for roll, ds in qdice.items():
                p2 = (f.p2 + roll) % 10 or 10
                if 21 <= f.score2 + p2:
                    p2_wins += ns * ps
                else:
                    new_state = state(p1, f.score1 + p1, p2, f.score2 + p2)
                    new_futures[new_state] += ns* ds * ps

    futures = new_futures

print(f"P2 {max(p1_wins, p2_wins) = }")
