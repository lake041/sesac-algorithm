from collections import deque
m,n,h = map(int, input().split())
graph, arr = [], []
for _ in range(h):
    for i in range(n):
        arr.append(list(map(int, input().split())))
    graph.append(arr)
    arr = []

dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k,i,j))

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append((nz, nx, ny))

answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                answer = -1
                break
            else:
                answer = max(answer, graph[k][i][j])
        if answer == -1:
            break
    if answer == -1:
        break

if answer == -1:
    print(answer)
else:
    print(answer-1)