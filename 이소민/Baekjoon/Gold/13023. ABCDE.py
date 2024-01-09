def dfs(idx, depth):
    global result
    visited[idx] = 1
    if depth == 4:
        result = 1
        return
    for i in graph[idx]:
        print(idx,depth)
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, depth+1)
            visited[i] = 0

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(n)]

result = 0
for i in range(n): 
    dfs(i,0)
    if result == 1:
        print(1)
        exit()
    visited[i] = 0
print(0)
