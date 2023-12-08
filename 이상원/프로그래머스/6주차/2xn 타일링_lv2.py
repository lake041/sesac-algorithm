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


print(solution(9))
print(solution2(9))