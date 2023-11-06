from collections import deque

# 1. 생각나는대로 푼 풀이
'''
def solution(priorities, location):
    x = []
    for i in range(len(priorities)):
        x.append(priorities[i])
        priorities[i] = (priorities[i], i)
    x.sort()
    priorities = deque(priorities)
    
    cnt = 0
    while True:
        priority, index = priorities.popleft()
        if x[-1] == priority:
            x.pop()
            cnt += 1
            if index == location:
                break
        else:
            priorities.append((priority, index))
        
    return cnt
'''

# 2. 깔끔한 풀이로 추가 예정