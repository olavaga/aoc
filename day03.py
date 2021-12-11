with open('data/day3.txt','r') as fil:
    data = fil.read().splitlines()

# Part one
most_common = ""
for i in range(len(data[0])):
    ones = sum(int(line[i]) for line in data)
    most_common += str(round(ones / len(data)))
least_common = "".join('1' if bit == '0' else '0' for bit in most_common)

print("Power consumption", int(most_common,2) * int(least_common,2))

# Part two
# Filter report data based on the bit criteria
def searchReport(bitCriteria):
    matches = data

    for i in range(len(data[0])):
        ones = sum(int(line[i]) for line in matches)
        bit = bitCriteria(ones, len(matches) - ones)
        matches = [line for line in matches if line[i] == bit]

        if len(matches) == 1:
            return int(matches[0],2)

oxygen_rating = searchReport(lambda ones, zeros: '1' if ones >= zeros else '0')
co2_scrubber = searchReport(lambda ones, zeros: '1' if ones < zeros else '0')

print("Life support rating", oxygen_rating * co2_scrubber)
