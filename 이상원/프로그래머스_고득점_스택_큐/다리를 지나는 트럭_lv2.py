from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    tw = deque(truck_weights)
    q = deque() # 다리에 있는 트럭
    q.append([1, tw.popleft()]) 
    time = 1
    while q:
        if len(tw)>0:
            pop = tw.popleft()
        else:
            while True: #다음 트럭 무게 + 다리에 있는 트럭 무게 > weight
                if len(q)==0: return time
                for i in range(len(q)):
                    q[i][0] += 1
                time += 1
                if q[0][0] == bridge_length +1:
                    q.popleft()

        bw = 0 # 다리에 있는 트럭 무게
        cnt_t = len(q) # 다리에 있는 트럭 갯수
        for i in range(len(q)):
            bw += q[i][1]
        sum_w = bw + pop # 다음 트럭 무게 + 다리에 있는 트럭 무게

        if sum_w <= weight: # 다음 트럭 무게 + 다리에 있는 트럭 무게 <= weight
            if cnt_t < bridge_length: # 다리에 있는 트럭 갯수 < bridge_length
                for w in q:
                    w[0] += 1
                if q[0][0] == bridge_length +1:
                    q.popleft()
                q.append([1, pop])
                time += 1
        else:
            while True: #다음 트럭 무게 + 다리에 있는 트럭 무게 > weight
                for i in range(len(q)):
                    q[i][0] += 1
                time += 1
                if q[0][0] == bridge_length +1:
                    q.popleft()
                    bw=0
                    
                    for i in range(len(q)):
                        bw += q[i][1]
                    sum_w = bw + pop
                    if sum_w <= weight:
                        q.append([1, pop])
                    else:
                        tw.append(pop)
                    break
        
        # 다음 트럭 무게 + 다리에 있는 트럭 무게 <= weight and 다리에 있는 트럭 갯수 < bridge_length -> q.append(pop) , time += 1, 다리를 다 지난 트럭 빼주기
        # 다음 트럭 무게 + 다리에 있는 트럭 무게 > weight -> time += 1
    return time

# 2	10	[7,4,5,6]

print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
def solution2(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
                 
         
    return answer




def solution3(bridge_length, weight, truck_weights):
    answer =0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    while bridge:
        answer+=1
        bridge.popleft()
        if len(truck_weights)>0:
            if sum(bridge) + truck_weights[0] <= weight:
                pop = truck_weights.popleft()
                bridge.append(pop)
            else:
                bridge.append(0)

    return answer

print(solution3(2,	10,	[7,4,5,6]))

print([0]*5)