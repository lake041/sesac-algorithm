import sys
from collections import deque
from itertools import product 
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
M, N = map(int, sys.stdin.readline().split()) # 가로 세로
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# for b in board:
#     print(b)

q = deque()
isAll = True
for i,j in product(range(N), range(M)):
    if board[i][j] == 1:
        q.append([i,j,0])
    if board[i][j] == 0:
        isAll = False
dx = [1,-1,0,0]
dy = [0,0,1,-1]
first_one_num = len(q)
# print(q)
answer = 0
if not isAll:
    while q: 
        x, y, day = q.popleft()
        answer = max(answer, day)
        for i,j in zip(dx, dy):
            nx, ny = x+i, y+j
            if 0 <= nx and nx < N and 0 <= ny and ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append([nx,ny,day+1])

    for i,j in product(range(N), range(M)):
        if board[i][j] == 0:
            answer = -1
            break
    print(answer)
else:
    print(0)





