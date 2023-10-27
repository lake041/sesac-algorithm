from collections import deque

dx = [1,0,0,-1,1,1,-1,-1]
dy = [0,1,-1,0,1,-1,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return 

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
