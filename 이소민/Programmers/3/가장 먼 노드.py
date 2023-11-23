from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    visited = [0] * (n+1)
    
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)
    
    m = max(visited)
    return visited.count(m)