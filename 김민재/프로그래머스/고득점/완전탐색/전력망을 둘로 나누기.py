from collections import deque
from sys import maxsize

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    nodes = set()
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        nodes.add(v1)
        nodes.add(v2)
    
    answer = maxsize
    for v1, v2 in wires:
        # 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        left, right = 0, 0
        visited = [False]*(n+1)
        
        # left
        q = deque()
        for start in range(1, n+1):
            if not visited[start] and start in nodes:
                q.append(start)
                visited[start] = True
                left += 1
                break
        
        while q:
            now = q.popleft()
            for next in graph[now]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    left += 1
        
        # right
        for start in range(1, n+1):
            if not visited[start] and start in nodes:
                q.append(start)
                visited[start] = True
                right += 1
                break
                
        while q:
            now = q.popleft()
            for next in graph[now]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    right += 1        
        
        # 원상복구
        graph[v1].append(v2)
        graph[v2].append(v1)
        
        answer = min(answer, abs(right-left))
        
    return answer