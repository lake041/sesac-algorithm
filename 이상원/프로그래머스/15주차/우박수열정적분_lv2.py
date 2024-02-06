def solution(k, ranges):
    answer = []
    
    dp = []
    temp=0
    while k!=1:
        temp = k
        if k%2 == 1:
            k = k*3 + 1
        else:
            k /= 2 
        dp.append((temp+k)/2)

    length = len(dp)
    for x,y in ranges:
        y += length
        if x>y:
            answer.append(-1.0)
        elif x==y:
            answer.append(0.0)
        else:
            answer.append(sum(dp[x:y]))

    return answer


print(solution(5,	[[0,0],[0,-1],[2,-3],[3,-3]]))