
import heapq

def solution(operations):
    
    lst = []
    lst2 = []
    for op in operations:
        sp = op.split(" ")
        if sp[0] == "I":
            heapq.heappush(lst, [int(sp[1]), -int(sp[1])])
            # heapq.heappush(lst2, "-" + sp[1])
        else:
            if lst:
                if sp[1] == "-1": #최소값 삭제
                    heapq.heappop(lst)
                
                else: #최댓값 삭제               
                    lst = change_heap(lst)
                    heapq.heappop(lst)
                    lst = change_heap(lst)
                
                    # heapq.heappop(lst2)    
    print(lst)
    answer = [0]*2
    if len(lst) >1:
        answer[1] = heapq.heappop(lst)[0]
        answer[0] = heapq.heappop(change_heap(lst))[1]
    elif len(lst) == 1:
        answer[0], answer[1] = heapq.heappop(lst)[0]
    elif len(lst) == 0:
        return answer
    
    print(answer) 

def change_heap(lst):
    temp = len(lst)
    lst2 = []
    if lst:
        for _ in range(temp):
            pop = heapq.heappop(lst)
            heapq.heappush(lst2, [pop[1], pop[0]])
    return lst2


# lst = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# print(solution(lst))


lst2 =[9,8,7,6,5]
heapq.heappush(lst2, 1)
print(lst2)
# lst2.sort()
# print(lst2)
# lst2 =[9,8,7,6,5]
# heappush(lst2, 1)
for _ in range(len(lst2)):
  print(heapq.heappop(lst2))
# print(sorted(lst2))