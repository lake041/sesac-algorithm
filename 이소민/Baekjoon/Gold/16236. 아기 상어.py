from collections import deque 

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y,size = 0,0,2

for i in range(n):
    for j in range(n):
        if board[i][j] ==9:
            x,y = i,j

def bfs(i,j,size):
    dist = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    tmp = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] =1
                    dist[nx][ny] = dist[x][y]+1
                    if board[nx][ny] < size and board[nx][ny] != 0:
                        tmp.append((nx,ny,dist[nx][ny]))
    return sorted(tmp, key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
answer = 0

while True:
    shark = bfs(x,y,size)
    if len(shark) == 0:
        break
    print(shark)
    nx,ny,dist = shark.pop()
    answer += dist
    board[x][y], board[nx][ny] = 0,0
    x,y = nx,ny
    cnt += 1
    if cnt == size:
        size+=1
        cnt = 0

print(answer)