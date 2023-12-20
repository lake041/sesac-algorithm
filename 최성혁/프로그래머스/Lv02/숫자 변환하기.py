'''
    X * 3n = y
    3a = 40 // X
    a = (40 // X) // 3 -> 1번

    X * 2a = 40
    2a = 40 // X
    a = (40 // X) // 2 -> 2번

    X + n*a = y
    a = (y-X) // n -> 3번
'''

# def solution(x, y, n):
#
#     resultList = []
#     if (y/x) % 3 == 0:
#         resultList.append((y//x) // 3)
#     if (y/x) % 2 == 0:
#         resultList.append((y//x) // 2)
#     if (y-x) % n == 0:
#         resultList.append((y-x) // n)
#     if not resultList:
#         resultList.append(-1)
#     answer = min(resultList)
#     return answer
#
#
# print(solution(10,40,30))

from collections import deque


def solution(x, y, n):
    answer = -1

    q = deque()

    q.append((x, 0))

    visited = set()

    while q:
        value, cnt = q.popleft()

        if value == y:
            answer = cnt
            break

        if value * 3 <= y and not value * 3 in visited:
            visited.add(value * 3)
            q.append((value * 3, cnt + 1))
        if value * 2 <= y and not value * 2 in visited:
            visited.add(value * 2)
            q.append((value * 2, cnt + 1))
        if value + n <= y and not value + n in visited:
            visited.add(value + n)
            q.append((value + n, cnt + 1))

    return answer
print(solution(10,40,30))