from collections import deque
def solution(board):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque()
    n = len(board)
    m = len(board[0])
    
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.':
                visited[i][j] = 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i,j,0))
    
    while q:
        x,y,cnt = q.popleft()
            
        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nx][ny] == '.' or board[nx][ny] == 'G' or board[nx][ny] == 'R':
                while board[nx][ny] == '.' or board[nx][ny] == 'G' or board[nx][ny] == 'R':
                    nx += dx[i]
                    ny += dy[i]
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        break
            
            a = nx-dx[i]
            b = ny-dy[i]
            
            if board[a][b] == 'G':
                return cnt+1

            if visited[a][b] == 0:
                visited[a][b] = 1
                q.append((a,b, cnt+1))
    return -1