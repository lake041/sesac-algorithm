from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    answer = 0
    _sum = 0
    while truck_weights:
        _sum -= bridge.popleft()
        if _sum + truck_weights[0] > weight:
            bridge.append(0)
        else:
            val = truck_weights.pop(0)
            bridge.append(val)
            _sum += val
        answer += 1
    answer += bridge_length
    return answer