import heapq
def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    time = 0
    hard_rest = True
    while jobs:
        if hard_rest:
            pop = heapq.heappop(jobs)
            time+=pop[1]            

        
    

    return answer

lst = [[0, 3],  [2, 6],[1, 9]]


heapq.heapify(lst)
# heapq.heappop(scoville)
print(lst[0])
heapq.heappop(lst)
print(lst)

