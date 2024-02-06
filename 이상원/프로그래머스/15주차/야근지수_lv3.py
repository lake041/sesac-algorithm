import heapq

def solution(n, works):
    works = list(map(lambda x:-x, works))
    heapq.heapify(works) 
    
    while n:
        if works:
            a = heapq.heappop(works)
        else:
            break
        a += 1
        if a:
            heapq.heappush(works, a)
        n-=1
         
    return sum(list(map(lambda x:x**2 ,works))) if works else 0

print(solution(4,[4, 3, 3]))