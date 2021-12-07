from math import floor

with open('day7.txt', 'r') as fil:
    crabs = list(map(int,fil.readline().split(',')))

crabs.sort()
mean = crabs[len(crabs)//2]
print("P1", sum(abs(it - mean) for it in crabs))

average = floor(sum(crabs) / len(crabs))
fuel_consumption = lambda n: sum(range(n+1))
print("P2", sum(fuel_consumption(abs(it - average)) for it in crabs))
