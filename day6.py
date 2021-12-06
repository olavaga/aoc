from collections import defaultdict, Counter

fish = None
with open('day6.txt', 'r') as fil:
    fish = Counter(map(int,fil.readline().strip().split(',')))

for i in range(256):
    next_gen = defaultdict(int)
    for i in range(9):
        if i:
            next_gen[i-1] += fish[i]
        else:
            next_gen[6] += fish[i]
            next_gen[8] += fish[i]

    fish = next_gen

print(sum(fish.values()))
        

