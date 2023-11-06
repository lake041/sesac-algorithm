from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    q = deque()
    q.append([1,truck_weights.popleft()])
    while q:
        
        curr_weight = 0
        for w in q:
            curr_weight += w[1]
        
        if bridge_length>len(q)
            for w in q:
                w[0] += 1
            

    return answer