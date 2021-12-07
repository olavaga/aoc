from math import floor
import statistics

with open('day7.txt', 'r') as fil:
    crabs = list(map(int,fil.readline().split(',')))

middle_crab = statistics.median(crabs)
print("P1", sum(abs(it - middle_crab) for it in crabs))

average = floor(statistics.mean(crabs))
fuel = lambda n: n*(n + 1)/2
print("P2", sum(fuel(abs(it - average)) for it in crabs))
