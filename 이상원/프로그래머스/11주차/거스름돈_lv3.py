from itertools import combinations
def solution(n, money):
    answer = 0
    for m in money:
        if n%m == 0:
            answer +=1 
    
    k = 2
    while k < len(money)+1:
        comb = list(combinations(money, k))
        for c in comb:
            sumc = sum(c)
            if sumc > n or max(c) > n:
                continue
            temp = n - sumc
            # nx + my = temp를 만족하는 0과 양의정수가 있음 됨(x,y) = c
            

        k+=1

    return answer

def money(comb, m):
    answer = 1
    if m == 0:
        return answer
    
    # 30  2 3 5 
    return answer


def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for typ in money :
        for price in range(typ, n+1) :
            dp[price] += dp[price - typ] 
    return dp[-1] % 1000000007



print(solution(5,[1,2,5]))
# solution(12,[1,3,5])
