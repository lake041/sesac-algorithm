from collections import deque
def solution(maps):
    answer = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    n = len(maps)
    m = len(maps[0])
    tmp = maps
    maps = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 'X':
                maps[i][j] = tmp[i][j]
            else:
                maps[i][j] = int(tmp[i][j])
    
    visited = [[0]*m for _ in range(n)]
    
    def bfs(i,j):
        arr = []
        q = deque()
        q.append((i,j))
        arr.append(maps[i][j])
        while q:
            x,y = q.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny<0 or ny >= m:
                    continue
                if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    arr.append(maps[nx][ny])
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        return sum(arr)
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(i,j))
    
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer