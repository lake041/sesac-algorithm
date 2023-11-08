from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        if len(scoville)-1 <= 0:
            answer = -1
            break
        a = heappop(scoville)
        b = heappop(scoville)
        item = a + 2*b
        heappush(scoville, item)
        answer += 1
    return answer
