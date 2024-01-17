# import sys
# from collections import defaultdict
# N, K = list(map(int, sys.stdin.readline().split()))

# prod = defaultdict(int)

# obj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]



# obj.sort()
# # print(obj)
# dp = [0 for i in range(K+1)]
# for w,v in obj:
#     dp[w] = max(v, dp[w])
#     if w > K:
#         break
# start = obj[0][0] +1

# for i in range(start, len(dp)):
#     tmp = dp[:i]
#     for j in range(1,int(i/2)+1):
#         a= i - j
#         if j == a:
#             break
#         dp[i] = max(dp[i],tmp[j] + tmp[a]) 
    
# print(dp[K])
# print(dp)


# dp[n] = max(dp[:n][m]+dp[:n][n-m]) # n>1  

import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

print(stuff)
#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
