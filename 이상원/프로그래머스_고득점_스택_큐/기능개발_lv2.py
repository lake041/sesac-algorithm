import math
from collections import deque
def solution(progresses, speeds):
    answer = []

    day = deque()
    for pro, spd in zip(progresses, speeds):
        day.append(math.ceil((100-pro)/spd))

    cnt = 1
    first = day.popleft()
    while day:
        pop = day.popleft()
        if first >= pop:
            cnt += 1
        else:
            first = pop
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)    

    return answer



print(solution([93, 30, 55],[1, 30, 5]))