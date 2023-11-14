from collections import deque
def solution(n, wires):
    l = []
    for k in range(1,n):
        wire = wires[:k-1]+wires[k:]
        
        graph = [[] for _ in range(n+1)]
        for i in wire:
            a, b = i[0], i[1]
            graph[a].append(b)
            graph[b].append(a)
            
        arr = []
        visited = [False]*(n+1)
        for j in range(n):
            if not visited[j]:
                arr.append(bfs(j, visited, graph))
        
        if len(arr) == 3:
            l.append(abs(arr[2]-arr[1]))

    return min(l)

def bfs(start, visited, graph):
    cnt = 0
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt