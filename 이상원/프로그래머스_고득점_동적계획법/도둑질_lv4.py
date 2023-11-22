def solution(money):
    ans1 = 0
    ans2 = 0
    if len(money)%2 == 0:
        for i in range(len(money)):
            if i%2 == 0:
                ans1 += money[i]
            else:
                ans2 += money[i]
        return max(ans1, ans2)
    
    pick = len(money)//2
    # while 1:


def solution2(money):
    answer = 0
    #첫 번째 집 포함, 마지막 집 비포함
    dp = [0 for _ in range(1000000+1)]
    dp[0] = 0
    dp[1] = money[0]
    #첫 번째 집 비포함, 마지막 집 포함
    dp2 = [0 for _ in range(1000000+1)]
    dp2[0] = 0
    dp2[1] = 0
    
    for i in range(2, len(money)+1):
        if i < len(money):
            dp[i] = max(dp[i-1], dp[i-2]+money[i-1])
            dp2[i] = max(dp2[i-1], dp2[i-2]+money[i-1])
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2]+money[i-1])
    
    answer = max(dp[len(money)-1], dp2[len(money)])
    return answer
