from itertools import combinations 
def solution(weights):
    return len([1 for i,j in list(combinations(weights, 2)) if i==j or i == j/2 or i == (2*j)/3 or i == (3*j)/4 or i == j*2 or i == (3*j)/2 or i == (4*j)/3])
print(solution([100,180,180,360,100,270]))
# print(solution([100,180,360,100,270]))
# print(solution([100,200,100,270,100]))


from collections import Counter
import math

def solution(weights):
    answer = 0
    # 1:1
    counter = Counter(weights)
    for k,v in counter.items():
        if v>=2:
            # answer+= v*(v-1)//2
            answer += math.comb(v, 2)
    weights = set(weights) 
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer
print(solution([100,180,180,360,100,270]))






# print(math.comb(100000,2))