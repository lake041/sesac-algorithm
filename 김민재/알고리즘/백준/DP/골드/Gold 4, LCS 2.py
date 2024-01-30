# https://www.acmicpc.net/problem/9252

from sys import stdin
input = stdin.readline

S1 = list(' ' + input().rstrip())
S2 = list(' ' + input().rstrip())

SL1 = len(S1)
SL2 = len(S2)

dp = [['']*SL1 for _ in range(SL2)]
for row in range(1, SL2):
    for col in range(1, SL1):
        if S1[col] == S2[row]:
            dp[row][col] = dp[row-1][col-1] + S1[col]
        else:
            if len(dp[row-1][col]) >= len(dp[row][col-1]):
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = dp[row][col-1]
print(len(dp[row][col]))
if len(dp[row][col]) >= 1:
    print(dp[row][col])