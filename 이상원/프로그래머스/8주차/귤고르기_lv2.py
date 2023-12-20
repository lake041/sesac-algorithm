from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    for tan in tangerine:
        dic[str(tan)] += 1
    dic2 = sorted(dic.items(), key= lambda x: x[1], reverse=True)
    for i,j in dic2:
        k -= j
        answer+=1
        if k<=0:
           return answer
            


    

solution(6,	[1, 3, 2, 5, 4, 5, 2, 3])
