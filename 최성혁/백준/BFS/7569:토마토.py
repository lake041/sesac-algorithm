from collections import deque


def bfs(v, start_list, tomato_board):
    dz = [0, 0, 0, 0, -1, 1]
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]

    q = deque()
    level = 0

    if len(start_list) != 0:
        while start_list:
            q.append(start_list.pop())

        while q:
            length = len(q)
            for _ in range(length):
                z, x, y = q.popleft()
                for i in range(6):
                    nz = z + dz[i]
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nz < H and 0 <= nx < M and 0 <= ny < N and tomato_board[nz][nx][ny] == 0 and not v[nz][nx][
                        ny]:
                        tomato_board[nz][nx][ny] = 1
                        v[nz][nx][ny] = True
                        q.append((nz, nx, ny))
            level += 1

        for i in range(H):
            for j in range(M):
                for k in range(N):
                    if tomato_board[i][j][k] == 0:
                        return -1

        return level
    else:
        return -1


# Input
N, M, H = map(int, input().split())
visited = [[[False] * N for _ in range(M)] for _ in range(H)]

tomato_board = []
start_list = []

for i in range(H):
    box = []
    for j in range(M):
        row = list(map(int, input().split()))
        box.append(row)
        for k in range(N):
            if row[k] == -1:
                visited[i][j][k] = True
            if row[k] == 1:
                start_list.append((i, j, k))
    tomato_board.append(box)

# Output
answer = bfs(visited, start_list, tomato_board)

if answer == -1:
    print(-1)
else:
    print(answer - 1)
