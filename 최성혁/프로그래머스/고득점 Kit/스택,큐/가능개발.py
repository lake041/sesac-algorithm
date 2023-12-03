from collections import deque
import math

def solution(progresses, speeds):
    answer = deque()
    for i in range(len(progresses)):
        currentLeftover = math.ceil((100 - progresses[i]) / speeds[i])
        answer.append(currentLeftover)

    val = answer.popleft()
    real = []
    cnt = 1
    for i in range(len(answer)):
        if answer[i] > val:
            val = answer[i]
            real.append(cnt)
            cnt = 1
        else:
            cnt += 1
    real.append(cnt)
    return real