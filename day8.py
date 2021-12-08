from aocd import data, submit

easy_digits = 0
total = 0

for line in data.splitlines():
    # Parse data
    uniq, display = line.split('|')
    uniq = set(uniq.split())
    display = display.split()

    easy_digits += sum(len(seg) in (2,4,3,7) for seg in display)

    # Sort signal patterns into an array
    ns = [""]*10
    
    # Length
    ns[1] = max(uniq, key=lambda n: len(n)==2)
    ns[4] = max(uniq, key=lambda n: len(n)==4)
    ns[7] = max(uniq, key=lambda n: len(n)==3)
    ns[8] = max(uniq, key=lambda n: len(n)==7)

    five_seg = set(filter(lambda n: len(n)==5, uniq))
    six_seg = set(filter(lambda n: len(n)==6, uniq))

    # Use sets to check if a number completely covers another number
    ns[3] = max(five_seg, key=lambda n: not set(ns[1]) - set(n))
    ns[6] = max(six_seg, key=lambda n: not set(ns[8]) - set(ns[7]) - set(n))
    ns[9] = max(six_seg, key=lambda n: not set(ns[4]) - set(n))

    # Assumes that 6, 9 and 5 are correctly discovered
    ns[5] = max(five_seg, key=lambda n: not set(n) - set(ns[6]))
    ns[2] = max(five_seg, key=lambda n: not set(ns[8]) - set(ns[9] + n))
    ns[0] = max(six_seg, key=lambda n: not set(ns[8]) - set(ns[5]) - set(n))

    # Check that all numbers have been found
    assert(len(set(ns)) == 10)

    # Read display and add to total
    num = ""
    for s in display:
        digit = max(range(10),key=lambda i:set(ns[i]) == set(s))
        num += str(digit)
        
    total += int(num)

print(easy_digits)
print(total)
submit(total)
