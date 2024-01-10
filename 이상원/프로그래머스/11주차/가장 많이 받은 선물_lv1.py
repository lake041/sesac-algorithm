from collections import defaultdict
from itertools import product
def solution(friends, gifts):
    answer = 0
    # 두명 중 선물 적게 받은 사람이 한개 받음
    # 선물지수 = 준거 - 받은거
    # 선물지수 작은놈 -> 큰놈
    # 선물지수까지 같으면 선물 안함
    n  = len(friends)
    gift = [[0 for i in range(n)] for _ in range(n)]
    index = defaultdict(int)
    for i in range(n):
        index[friends[i]] = i
    
    # print(index)
    
    for g in gifts:
        se, re = g.split()
        x,y = index[se],index[re]
        gift[x][y] +=1
    
    # print(gift)
    gi1 = [sum(i) for i in gift]
    gi2 = [sum(j) for j in zip(*gift)]
    gi = [i-j for i,j in zip(gi1,gi2)]
    
    # print(gi)
    answer = [0 for _ in range(n)]
    for i,j in product(range(n),range(n)):
        if i<=j:
            continue
        a, b = gift[i][j],gift[j][i]     
        
        if a == b:
            if gi[i] > gi[j]:
                answer[i]+=1
            elif gi[i] < gi[j]:
                answer[j]+=1
            
        elif a > b:
            answer[i]+=1
        elif a < b:
            answer[j]+=1
            
    return max(answer)