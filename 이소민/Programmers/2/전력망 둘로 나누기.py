# bfs 풀이
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


# dfs 풀이
def dfs(start):
    visited[start] = 1
    node = 1
    for i in graph[start]:
        if visited[i] == 0:
            node += dfs(i)
    return node
            
def solution(n, wires):
    answer = -1
    global graph
    graph = [[] for _ in range(n+1)]
    global visited
    visited = [0]*(n+1)
    for w in wires:
        a,b = w
        graph[a].append(b)
        graph[b].append(a)
    ans_list = []
    for w in wires:
        a,b = w
        visited = [0]*(n+1)
        # 단선
        graph[a].remove(b)
        graph[b].remove(a)
        # 그룹1 노드 개수
        group1 = dfs(a)
        # 그룹2 노드 개수
        group2 = dfs(b)
        gap = abs(group1 - group2)
        ans_list.append(gap)
        
        # 선복구
        graph[a].append(b)
        graph[b].append(a)
    return min(ans_list)