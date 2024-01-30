from collections import deque

def is_valid(x, y, field, visited):
    return 0 <= x < len(field) and 0 <= y < len(field[0]) and field[x][y] == 1 and visited[x][y] == -1

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    field = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                field[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited = [[-1] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 0

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny, field, visited):
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer
