from collections import deque

def bfs(x,y,board):
    q = deque()
    q.append([x,y])
    board[x][y] = 0
    # level 탐색을 위한
    L = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        length = len(q)
        for i in range(length):
            qx,qy = q.popleft()
            for j in range(4):
                nx = qx + dx[j]
                ny = qy + dy[j]
                if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
                    q.append([nx,ny])
                    board[nx][ny] = 0
        L += 1
    print(L)











board = [
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0]
]

answer = 0
for i in range(5):
    for j in range(5):
        if board[i][j] == 1:
            bfs(i,j,board)
            answer += 1

print(answer)
