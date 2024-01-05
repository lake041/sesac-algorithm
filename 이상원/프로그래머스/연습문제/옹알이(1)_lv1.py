from itertools import permutations
def solution(babbling):
    answer = 0
    ong=["aya","ye","woo","ma"]
    for i in range(4):
        a = ["".join(p) for p in list(permutations(ong,i+1))]
             
        for b in babbling:
                if b in a:
                    answer+=1        
    return answer
