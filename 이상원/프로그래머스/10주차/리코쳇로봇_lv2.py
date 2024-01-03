from collections import deque

def solution(board):
    answer = -1
    r,c = len(board), len(board[0])
    
    q = deque()
    visited = [[0 for _ in range(c)] for _ in range(r)]
    # visited = [[0 for i in range(c)] for j in range(r)]
    g = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == "D":
                visited[i][j] = 1
            elif board[i][j] == "R":
                q.append([i,j,0])
                visited[i][j] = 1
            elif board[i][j] == "G":
                g = [i,j]
    
    g1,g2 = g
    cnt = 0
    for nx,ny in zip([g1+1, g1-1,g1,g1],[g2,g2,g2+1,g2-1]):
        if 0<=nx<r and 0<=ny<c and board[nx][ny] == ".":
            cnt +=1
    if cnt ==4:
        return -1
    dx =[1,-1,0,0]
    dy =[0,0,1,-1]
    while q:
        x,y,ans = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] != "D":
                while 1:
                    nx += dx[i]
                    ny += dy[i]
                    if not (0<=nx<r and 0<=ny<c) or board[nx][ny] == "D":
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if visited[nx][ny]:
                    continue
                if [nx, ny] == g:
                    return ans+1
                visited[nx][ny] = 1
                q.append([nx,ny, ans+1])
    
    return answer