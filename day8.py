from aocd import data, submit

easy_digits = 0
total = 0
for line in data.splitlines():
    uniq, outputs = line.split('|')
    easy_digits += sum(len(seg) in (2,4,3,7) for seg in outputs.split())
    uniq = uniq.split()
    outputs = outputs.split()

    ns = [""]*10
    ns[1] = [n for n in uniq if len(n) == 2][0]
    ns[4] = [n for n in uniq if len(n) == 4][0]
    ns[7] = [n for n in uniq if len(n) == 3][0]
    ns[8] = [n for n in uniq if len(n) == 7][0]

    # 0, 6 and 9
    group = [n for n in uniq if len(n) == 6]
    ns[9] = [n for n in group if not set(ns[4]) - set(n)][0]
    group = [n for n in group if n not in ns]
    ns[0] = [n for n in group if not set(ns[1]) - set(n)][0]
    ns[6] = [n for n in group if not n in ns][0]

    # 2, 3, 5
    group = [n for n in uniq if len(n) == 5]
    ns[3] = [n for n in group if not set(ns[1]) - set(n)][0]
    ns[5] = [n for n in group if not set(n) - set(ns[6])][0]
    ns[2] = [n for n in group if not n in ns][0]

    number = "".join([str(i) for i,n in enumerate(ns) if set(n)==set(s)][0]for s in outputs)
    total += int(number)

    

print(easy_digits)
submit(total)
    
