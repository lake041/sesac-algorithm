def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles: continue
            if i-1 >=1 and [j,i-1] not in puddles:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 1 and [j-1,i] not in puddles:
                dp[i][j] += dp[i][j-1]
    return dp[-1][-1] % 1000000007