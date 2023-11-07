from collections import deque
def solution(priorities, location):
    q = deque()
    answer = 0
    for i, val in enumerate(priorities):
        q.append((i, val))
    while q:
        _max = max(q, key= lambda x: x[1])[1]

        cur = q.popleft()
        if _max > cur[1]:
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer