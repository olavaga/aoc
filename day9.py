from aocd import data, submit

area = [list(l) for l in data.splitlines()]
adj = [(1,0),(-1,0),(0,1),(0,-1)]
lows = []

for i, line in enumerate(area):
    for j, ch in enumerate(line):
        low = int(ch) + 1
        for m,n in adj:
            if 0<=i+m<len(area) and 0<=j+n<len(area[0]):
                low = min(low,int(area[i+m][j+n]))
        if low > int(ch):
            lows.append((i,j))

basins = []
for p in lows:
    basin = set((p,))
    while True:
        nb = set()
        
        for q in basin:
            for m,n in adj:
                i,j=q
                if 0<=i+m<len(area) and 0<=j+n<len(area[0]):
                    if area[i+m][j+n] == '9':
                        continue
                    if int(area[i+m][j+n]) > int(area[i][j]):
                        nb.add((i+m,j+n))
        if not nb - basin:
            break
        basin.update(nb)
    basins.append(basin)

basins.sort(key=len, reverse = True)
a,b,c,*basins = basins

print(len(lows))
print("P1",sum(int(area[i][j])+1 for i,j in lows))
print(len(a),len(b),len(c))
submit(len(a)*len(b)*len(c))

