from collections import deque


def bfs(v, start_list, tomato_board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    level = 0

    if len(start_list) != 0:

        while start_list:
            q.append(start_list.pop())

        while q:
            length = len(q)
            for _ in range(length):
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N and tomato_board[nx][ny] == 0 and not v[nx][ny]:
                        tomato_board[nx][ny] = 1
                        v[nx][ny] = True
                        q.append((nx, ny))
            level += 1

        for i in range(M):
            for j in range(N):
                if tomato_board[i][j] == 0:
                    return -1

        return level
    else:
        return -1


N, M = map(int, input().split())
visited = [[False] * N for _ in range(M)]

tomato_board = []
start_list = []

for i in range(M):
    row = list(map(int, input().split()))
    tomato_board.append(row)
    for j in range(N):
        # -1일떄 방문 리스트 방문처리
        if row[j] == -1:
            visited[i][j] = True
        # 1일경우 startList에 추가
        if row[j] == 1:
            start_list.append((i, j))

answer = bfs(visited, start_list, tomato_board)

if answer == -1:
    print(-1)
else:
    print(answer-1)
