computer = int(input())
connect = int(input())

graph = [[]for i in range(computer + 1)]

# 방문배열
visited = [False] * (computer+1)

visited[0] = True

for _ in range(connect):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            # 1번 노드와 연관있는 count
            cnt += 1
            dfs(i,visited)



cnt = 0
dfs(1,visited)
print(cnt)