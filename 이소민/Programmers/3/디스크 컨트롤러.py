# 복습 필요 
from heapq import *
def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    q = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(q, [job[1], job[0]])
        if len(q) > 0:
            cur = heappop(q)
            start = now
            now += cur[0]
            answer += (now - cur[1])
            i += 1
        else:
            now += 1
    return answer // len(jobs)