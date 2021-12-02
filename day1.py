
inc = 0
pr = [int(input()) for i in range(3)]
for _ in range(1997):
    n = int(input())
    if sum(pr) < sum(pr[1:],n):
        inc += 1
    pr = pr[1:] + [n]
print(inc)

