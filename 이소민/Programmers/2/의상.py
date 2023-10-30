def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 1
        else:
            dict[i[1]] += 1
    
    for i in dict.values():
        answer *= (i+1)
    return answer-1