from itertools import permutations


def isPrime(str):
    # 0 제외
    if str[0] == '0':
        return
    num = int(str)
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        # 순열로 경우의 수 나열 
        for j in list(permutations(numbers, i)):
            arr = list(j)
            # str 변환
            st = ''.join(arr)
            # 소수인지 확인
            if isPrime(st):
                # 1 제외
                if st == '1':
                    continue
                answer.append(st)

    # 중복 제거
    return len(set(answer))


print(solution("17"))