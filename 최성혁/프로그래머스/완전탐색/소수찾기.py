import math


def isPrime(n):
    if n == 1:  # 1은 약수가 아니므로 제외
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근까지 약수가 존재하는지 확인
            if n % i == 0:  # 약수가 존재하면 False
                return False
        return True  # 존재하지 않으면 True


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if isPrime(i):
            answer += 1
    return answer
