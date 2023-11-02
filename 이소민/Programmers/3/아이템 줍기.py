from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0]*102 for _ in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for x in range(x1, x2+1):
            maps[x][y1] = 1
            maps[x][y2] = 1
        for y in range(y1, y2+1):
            maps[x1][y] = 1
            maps[x2][y] = 1
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                maps[x][y] = 0
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append((characterX*2, characterY*2))
    maps[characterX*2][characterY*2] = 0
    while q:
        x,y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return maps[itemX*2][itemY*2] // 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 102 or ny <0 or ny >= 102:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))