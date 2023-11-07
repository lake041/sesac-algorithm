from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    currentWeight = 0
    while len(truck_weights) != 0:
        time += 1
        # 1초 지날 때마다 하나씩 빠짐.
        currentWeight -= bridge.popleft()

        # weight 이하일때
        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        # weight 이상일때
        else:
            bridge.append(0)

    time += bridge_length

    return time


solution(2,10,[7,4,5,6])