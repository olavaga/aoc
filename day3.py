
with open('day3.txt','r') as fil:
    data = fil.readlines()

sums = [0]*12
total = 0
first_bits = []
for line in data:
    sums = [int(ch) + init for ch, init in zip(line, sums)]
    total += 1

most_common = "".join(str(round(sums[i] / total)) for i in range(12))
least_common = "".join(str(round(1 - sums[i] / total)) for i in range(12))

matches = data
index = 0
while 1 < len(matches):
    ones = sum(int(line[index]) for line in matches)
    zeros = sum(1 - int(line[index]) for line in matches)
    bit = '1' if ones >= zeros else '0'
    matches = [line for line in matches if line[index] == bit]
    index += 1

oxygen_rating = int(matches[0],2)

matches = data
index = 0
while 1 < len(matches):
    ones = sum(int(line[index]) for line in matches)
    zeros = sum(1 - int(line[index]) for line in matches)
    bit = '1' if ones < zeros else '0'
    matches = [line for line in matches if line[index] == bit]
    index += 1

co2_scrubber = int(matches[0], 2)

print("Power consumption", int(most_common,2) * int(least_common,2))

print("Life support rating", oxygen_rating * co2_scrubber)
