# 합계: 75.0 / 100.0
# -> 시간초과
# def isConsecutiveNumber(number, n):
#     target = 0
#     while number <= n:
#         target += number
#         if target == n:
#             return True
#         number += 1
#     return False
#
#
# def solution(n):
#     answer = 0
#     for i in range(1, n):
#         if isConsecutiveNumber(i, n):
#             answer += 1
#         else:
#             pass
#
#     return answer
#
#
# print(solution(15))

#  시간초과
#
# def solution(n):
#     answer = 0
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 3
#
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + i
#
#     for num in dp:
#         if num == n:
#             answer += 1
#         elif num > n:
#             target = num - n
#             print(target)
#             if target in dp:
#                 answer += 1
#
#     return answer

def isConsecutiveNumber(number, n):
    target = 0
    while number <= n:
        target += number
        if target == n:
            return True
        if target > n:
            return False
        number += 1
    return False


def solution(n):
    answer = 0
    for i in range(1, n):
        if isConsecutiveNumber(i, n):
            answer += 1
        else:
            pass

    return answer + 1

