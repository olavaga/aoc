with open('data/day1.txt', 'r') as fil:
    inc = 0
    pr = [int(fil.readline()) for i in range(3)]
    for _ in range(1997):
        n = int(fil.readline())
        if sum(pr) < sum(pr[1:],n):
            inc += 1
        pr = pr[1:] + [n]
    print(inc)

