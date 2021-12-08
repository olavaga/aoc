from aocd import data, submit

def select(fn, lst):
    selected = [n for n in lst if fn(n)]
    other = [n for n in lst if not fn(n)]
    return selected, other

easy_digits = 0
total = 0

for line in data.splitlines():
    uniq, display = line.split('|')
    uniq = uniq.split()
    display = display.split()

    easy_digits += sum(len(seg) in (2,4,3,7) for seg in display)

    # Sort signal patterns into an array
    ns = [""]*10
    
    # Length
    ns[1], uniq = select(lambda n: len(n)==2, uniq)
    ns[4], uniq = select(lambda n: len(n)==4, uniq)
    ns[7], uniq = select(lambda n: len(n)==3, uniq)
    ns[8], uniq = select(lambda n: len(n)==7, uniq)

    group1, group2 = select(lambda n: len(n)==6, uniq)

    # 0, 6 and 9 - which number covers which?
    ns[9], group1 = select(lambda n: not set(*ns[4]) - set(n), group1)
    ns[0], ns[6] = select(lambda n: not set(*ns[7]) - set(n), group1)

    # 2, 3 and 5
    ns[3], group2 = select(lambda n: not set(*ns[1]) - set(n), group2)
    ns[5], ns[2] = select(lambda n: not set(n) - set(*ns[6]), group2)

    # Flatten
    ns = [n[0] for n in ns]

    num = ""
    for s in display:
        digit = [i for i,n in enumerate(ns) if set(n) == set(s)][0]
        num += str(digit)
        
    total += int(num)

print(easy_digits)
print(total)
