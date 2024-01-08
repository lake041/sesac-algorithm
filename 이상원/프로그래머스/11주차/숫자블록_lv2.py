def maxdivisor(n):
    if n == 1:
        return 0
    
    divisors = []
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            if x <= 1e7:
                divisors.append(x)
            if n // x <= 1e7 and n // x != n and (x**2) != n:
                divisors.append(n//x)
    
    return max(divisors)

def solution(begin, end):
    # 규칙성을 파악해보면,
    # 배열의 n번째 원소는 자기 자신이 아닌 가장 큰 약수가 됨
    # 주의) 10000000까지의 숫자가 적힌 블록들을 이용했으므로,
    # 자기 자신이 아니면서, 10000000 이하의 가장 큰 약수를 구해야 합니다.
    answer = [maxdivisor(n) for n in range(begin, end+1)]
    return answer

solution(1,10)

print(6**0.5)
print(1e7)


def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            tmp = (i**2) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

getMyDivisor(16)

