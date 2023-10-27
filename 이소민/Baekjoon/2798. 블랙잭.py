from itertools import combinations

n, m = map(int, input().split())

# combinations 사용해서 모든 경우의 수 구함 
nums = list(combinations(list(map(int, input().split())), 3))
arr = []
# 모든 경우의 수의 합 
for i in nums:
    arr.append(sum(i))

# 내림차순으로 정렬하여 m보다 작거나 같으면 반환하고 break
arr.sort(reverse=True)
for i in arr:
    if i <= m:
        print(i)
        break