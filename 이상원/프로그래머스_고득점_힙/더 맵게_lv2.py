import heapq
def scoville_return(a, b):
    sco = a+(b*2)
    return sco

def solution(scoville, K):
    sco = 0
    
    heapq.heapify(scoville)
    if scoville[0] >=K:
        return 0;
    cnt = 0
    while(True):
        if(len(scoville)>1):
            sco=heapq.heappop(scoville)
            heapq.heappush(scoville, scoville_return(sco, heapq.heappop(scoville)))
            cnt+=1
        else:  
            return -1
        if scoville[0] >= K:
            return cnt
        
