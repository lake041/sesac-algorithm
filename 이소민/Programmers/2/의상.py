from itertools import combinations

def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 1
        else:
            dict[i[1]] += 1
    
    for i in range(1,len(dict)+1):
        for j in list(combinations(dict, i)):
            tmp = 1
            for k in j:
                tmp *= dict[k]
            answer += tmp
    return answer-1