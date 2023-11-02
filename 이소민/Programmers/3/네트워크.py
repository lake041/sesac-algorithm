from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    visited = []
    for i in range(n):
        if i not in visited:
            q.append(i)
            answer += 1
            
            while q:
                cur = q.popleft()
                for j in range(n):
                    if computers[cur][j] == 1 and j not in visited:
                        q.append(j)
                        visited.append(j)
    return answer