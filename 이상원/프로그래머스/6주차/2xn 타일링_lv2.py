import math
def solution(n):
    if n%2 == 1:
        return ((int(math.pow(2,int((n-1)/2))+1))*2)%1000000007
    else:
        return int(math.pow(2,n/2)+1)%1000000007


def solution2(n):
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, (a + b) % 1000000007
    return b

def solution3(n):
    
    dp = [1 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[-1]


# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 8
print(solution(9))
print(solution2(9))