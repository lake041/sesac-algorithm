from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))

seven = list(combinations(arr, 7))

for i in seven:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break