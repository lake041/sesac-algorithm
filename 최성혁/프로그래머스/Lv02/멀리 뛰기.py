'''
 칸의수가 1개 ~ n개일때까지 중복을 허용하여(itertools product 사용) -> 시간초과
'''

def solution(n):
    # 1일떄 그냥 return
    if n == 1:
        return 1 % 1234567
    # 2일때 그냥 return
    elif n == 2:
        return 2 % 1234567
    else:
        # 나머지 경우
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        # A[N] = A[N-1] + A[N-2]
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1] % 1234567



