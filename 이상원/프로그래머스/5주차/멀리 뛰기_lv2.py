
import math
def solution(n):
    answer = 0
    r = 0
    while 1:
        comb=math.comb(n,r)
        if (comb ==0):
            return answer%1234567
        answer += comb
        n -=1
        r +=1 


# print(solution())
print(math.comb(2,4))

# 2칸이 0개인 경우 - 1개
# 2칸이 1개인 경우 - n-1개
# 2칸이 2개인 경우 - n -> 홀수면 n/2+1개