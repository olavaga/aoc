from aocd import data, submit
from collections import Counter

# Generate a unique number for each segment based on occurrences and the
# length of the word it occurs in.
segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", 
            "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
freqs = Counter("".join(p*len(p)**2 for p in segments))
ordering = sorted("abcdefg", key=freqs.get)

easy_digits = 0
total = 0

for line in data.splitlines():
    # Parse data and generate numbers for each symbol
    uniq, display = line.split('|')
    uniq_freqs = Counter("".join(p*len(p)**2 for p in uniq.split()))

    # Create table and translate display
    ordering_uniq = map(ord,sorted("abcdefg", key=uniq_freqs.get))
    display = display.translate(dict(zip(ordering_uniq, ordering)))

    # Read and add display to total
    display = ("".join(sorted(p)) for p in display.split())
    number = "".join(map(str,map(segments.index, display)))

    easy_digits += sum(n in "1478" for n in number)
    total += int(number)

print(easy_digits)
submit(total)
