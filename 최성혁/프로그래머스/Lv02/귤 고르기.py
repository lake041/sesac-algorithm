# '''
#     1. 크기별로 몇개인지 cnt
#     2. key값 기준으로 내림차순 sort
#     3. k가 0이 될때까지 "뺀다" (딱 맞게 떨어질 필요 X)
#     3-1. 내림차순 했으니 앞에서부터 ?
#     dict_a={'파이썬':1, '자바':2, '자바스크립트':3, '씨':4}
#     sorted_dict = sorted(dict_a.items(), key= lambda item:item[1])
# '''
# [1]
# 26.5 / 100.0
# def solution(k, tangerine):
#     numbers = set(tangerine)
#     tangerineDic = dict()
#     for i in numbers:
#         tangerineDic[i] = tangerine.count(i)
#     resultDic = sorted(tangerineDic.items(),key = lambda x : x[1],reverse=True)
#     answer = 0
#     for target in resultDic:
#         if target[1] < k:
#             k -= target[1]
#             answer += 1
#         if k < 0:
#             break
#
#     return answer
# [2]
# 82.4 / 100.0 -> 시간초과 4개 테스트 케이스
# def solution(k, tangerine):
#     numbers = set(tangerine)
#     tangerineDic = dict()
#     for i in numbers:
#         tangerineDic[i] = tangerine.count(i)
#     resultDic = sorted(tangerineDic.items(), key=lambda x: x[1], reverse=True)
#     answer = 0
#     for target in resultDic:
#         if target[1] < k:
#             k -= target[1]
#             answer += 1
#         else:
#             break
#
#     return answer+1

from collections import Counter


def solution(k, tangerine):
    # 1. tangerine 리스트에서 각 요소의 등장 횟수를 계산합니다.
    tangerine_counts = Counter(tangerine)
    print(tangerine_counts)
    # 2. 등장 횟수를 기준으로 내림차순으로 정렬된 리스트를 생성합니다.
    resultDic = sorted(tangerine_counts.items(), key=lambda x: x[1], reverse=True)
    print(resultDic)

    # 3. 정렬된 리스트를 순회하면서 k를 만족시키기 위해 요소를 제거합니다.
    answer = 0
    for target in resultDic:
        if target[1] < k:
            k -= target[1]
            answer += 1
        else:
            break  # k가 0 이하가 되면 루프를 종료합니다.

    return answer + 1

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))



from collections import defaultdict

def solution(k, tangerine):
    numbers = set(tangerine)
    tangerineDic = defaultdict(int)
    for i in tangerine:
        tangerineDic[i] += 1

    resultDic = sorted(tangerineDic.items(), key=lambda x: x[1], reverse=True)

    answer = 0
    for target in resultDic:
        if target[1] < k:
            k -= target[1]
            answer += 1
        else:
            break

    return answer+1