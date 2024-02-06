'''
2 3 4
 []
'''

# def solution(weights):
#     answer = 0
#     resultlst = []
#     for i in range(len(weights)):
#         # 잘린 앞부분
#         tmp_first = []
#         # 잘린 뒷부분
#         tmp_second = []
#         # 타겟 value
#         target = weights[i]
#
#         if i == 0:
#             tmp_second = weights[i + 1:]
#             # print(tmp_second)
#         else:
#             tmp_second = weights[i + 1:]
#             tmp_first = weights[:i]
#             # print(tmp_first,tmp_second)
#         resulttmp = tmp_first + tmp_second
#
#         if target in resulttmp:
#             resultlst.append([target, target])
#         elif target * 2 in resulttmp:
#             resultSet.add((target * 2, target))
#         elif target * 3 in resulttmp:
#             resultSet.add((target * 3, target))
#         elif target * 4 in resulttmp:
#             resultSet.add((target * 4, target))
#
#     print(reusltlst)
#     return answer

from collections import Counter


def solution(weights):
    answer = 0

    # 1:1
    counter = Counter(weights)
    for key, value in counter.items():
        if value >= 2:
            answer += value * (value - 1) // 2

    weights = set(weights)  # 1:1 구한 후 중복 제거

    # 2:3, 2:4, 3:4
    for w in weights:
        if w * 2 / 3 in weights:
            answer += counter[w * 2 / 3] * counter[w]
        if w * 2 / 4 in weights:
            answer += counter[w * 2 / 4] * counter[w]
        if w * 3 / 4 in weights:
            answer += counter[w * 3 / 4] * counter[w]
    return answer