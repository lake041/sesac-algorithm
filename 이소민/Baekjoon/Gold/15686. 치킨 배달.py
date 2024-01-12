from itertools import combinations
n,m = map(int,input().split())
city = []
for i in range(n):
    city.append(list(map(int,input().split())))

chicken = []
resident = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i,j])
        if city[i][j] == 1:
            resident.append([i,j])
chicken_distance = []

for cand in combinations(chicken, m):
    distance = 0
    distance_cand = []
    for r in resident:
        for c in cand:
            x1,y1 = r
            x2, y2 = c
            distance_cand.append(abs(x1-x2)+abs(y1-y2))
        distance += min(distance_cand)
        distance_cand = []
    chicken_distance.append(distance)
print(min(chicken_distance))
