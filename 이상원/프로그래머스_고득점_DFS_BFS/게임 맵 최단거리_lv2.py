from collections import deque
def solution(maps):
    n = len(maps) # x
    m = len(maps[0]) # y
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append([0,0])
    dx = [-1, 1 ,0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0] =True
    while queue:
        x, y = queue.popleft() # 0, 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< n and 0 <= ny < m and maps[nx][ny] == 1:
                if visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1

    return maps[n-1][m-1] if maps[n-1][m-1] !=1 else -1 





print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))