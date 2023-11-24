from collections import deque
N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]

visited = [True] * (N+1)

# 인접리스트 초기화
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
#print(graph)
def dfs(start,graph):
    visited[0] , visited[start] = False,False
    #print('dfs visit : ',visited)
    print(start,end=' ')
    for i in graph[start]:
        if visited[i]:
            visited[i] = False
            dfs(i,graph)




def bfs(graph):
    queue = deque()
    queue.append(V)
    visited[0],visited[V] = False,False
    #print('bfs visit : ',visited)
    while queue:
        val = queue.popleft()
        print(val,end=' ')
        for i in graph[val]:
            if visited[i]:
                visited[i] = False
                queue.append(i)


dfs(V,graph)
print()
visited = [True] * (N+1)
visited[0] = False
bfs(graph)