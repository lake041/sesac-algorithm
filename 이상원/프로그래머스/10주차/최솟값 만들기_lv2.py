import heapq
def solution(A,B):
    answer = 0
    for i in range(len(B)):
        B[i] = -1*B[i]
    heapq.heapify(A)    
    heapq.heapify(B)
    
    while A:
        answer += heapq.heappop(A)*heapq.heappop(B)

    return answer*-1

solution([1, 4, 2],[5, 4, 4])