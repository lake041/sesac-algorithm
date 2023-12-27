from collections import deque
m,n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

answer = 0
for i in graph:
    if 0 in i:
        answer = 0
        break
    answer = max(answer, max(i))

print(answer-1)