from collections import deque

def bfs(maps, x, y, row, column, v):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    q.append([x, y])
    maps[x][y] = 0
    v[x][y] = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < row and 0 <= ny < column and maps[nx][ny] != 0:
                if v[nx][ny] == -1:
                    v[nx][ny] = 1
                    maps[nx][ny] = maps[a][b] + 1
                    q.append([nx, ny])

    for i in range(row):
        for j in range(column):
            if v[i][j] == -1:
                maps[i][j] = -1
    return maps

n, m = map(int, input().split())
maps = []
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    lst = list(map(int, input().split()))
    maps.append(lst)
    for j in range(m):
        if maps[i][j] == 2:
            x, y = i, j
        if maps[i][j] == 0:
            visited[i][j] = 0

result = bfs(maps, x, y, n, m, visited)

for row in result:
    for val in row:
        print(val, end=" ")
    print()
