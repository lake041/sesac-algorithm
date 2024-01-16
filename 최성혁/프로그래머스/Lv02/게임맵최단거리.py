from collections import deque


def bfs(maps):
    row = len(maps)
    column = len(maps[0])
    if maps[row - 1][column] == 0 and maps[row][column - 1] == 0 and maps[row - 1][column - 1] == 0:
        return -1
    visited = [[False] * column for _ in range(row)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append([0, 0, 0])
    level = 0

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < column and 0 <= ny < row and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append([nx, ny, cnt + 1])
                print(q)
    return cnt


def solution(maps):
    answer = bfs(maps)

    return answer
