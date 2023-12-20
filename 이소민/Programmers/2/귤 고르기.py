from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for i in tangerine:
        dict[i] += 1
    
    dict = sorted(dict.items(), key =lambda x: x[1], reverse=True)
    sum, cnt = 0, 0
    for i in dict:
        if sum >= k:
            break
        sum += i[1]
        cnt += 1
    answer = cnt
    
    return answer